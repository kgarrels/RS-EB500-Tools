#!/usr/bin/env python

#Copyright 2015 Kai Garrels
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#


import telnetlib
import socket
import struct
import pyaudio
import sys
import termios
import stat, os, datetime


EB500_ADDR = '192.168.2.5'
CMD_PORT = 5555
UDP_PORT = 19000
TCP_PORT = 5565


class Eb500Cmd (telnetlib.Telnet):
    def __init__(self, host=None, port=0):
        self = telnetlib.Telnet.__init__(self,host, port)

    def send_cmd(self, cmd):
        print "> "+ cmd
        self.write(cmd+"\n")
        ans = self.read_eager()     # FIXME: does not receive anything
        #print "< " + ans
        return ans


def StrToHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
        lst.append(" ")
    return reduce(lambda x,y:x+y, lst)

def OwnIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip = (s.getsockname()[0])
    s.close()
    return ip

def parseMessage(msg):
    global eb200_magic, eb200_sequence, packets, lost, old_header

    err = None
    # decode eb200 header
    magic, ver_min, ver_maj, seq_low, seq_high, data_Size =  struct.unpack('!LHHHHL', msg[0:16])     # eb200 header
    if (eb200_magic == 0) & (magic == 0x0EB200):
        print "received 1st EB200 frame, version ",ver_maj,".",ver_min
        eb200_magic=magic

    if eb200_sequence != seq_low-1:
        lost = lost +1
        print "***** lost packet, ", lost, " of ", packets
    eb200_sequence = seq_low
    packets = packets+1

    # decode generic attribute
    tag, length = struct.unpack('!HH', msg[16:20])          # generic attribute, we need the tag


    # decode attribute according to tag
    if tag == 401:  # audio
        frame_count, reserved, opt_header_length, selector_flags = struct.unpack('!HcBL', msg[20:28])
        #print "frames: ", frame_count
        if opt_header_length != 0:
            #print "opt header length: ", opt_header_length, "msg length: ", len(msg)
            opt_header = struct.unpack('<hhLLH8sL6sQh', msg[28:28+opt_header_length])
            if (opt_header[0:7] != old_header[0:7]) & (opt_header[0]) == 1:
                time = datetime.datetime(1970,1,1) + datetime.timedelta(microseconds=opt_header[8]/1000)       #audio time stamp
                print "audio", (opt_header[2]/1e6).__format__(".5f"), "MHz", opt_header[5].split('\x00')[0], opt_header[3]/1e3, "kHz", \
                      "latency", (datetime.datetime.utcnow()-time).microseconds / 1000, "ms"
                old_header = opt_header
        # output, assume audio mode 1. Audio goes to default device and soundflower in parallel
        err = audio_stream.write(msg[28+opt_header_length:])
        if err != None:
            print "pyudio write error: ", err
#        err = sndfl_stream.write(msg[28+opt_header_length:])
        if err != None:
            print "pyudio write error: ", err
    elif tag == 501:  # IFPan
        frame_count, reserved, opt_header_length, selector_flags = struct.unpack('!HcBL', msg[20:28])
        #print "frames: ", frame_count
        if opt_header_length != 0:
            #print "opt header length: ", opt_header_length, "msg length: ", len(msg)
            opt_header = struct.unpack('<LLhhLLlLLQLLhhQ', msg[28:28+opt_header_length])
            #print "opt header: ", opt_header
        # now we have the values
        if_pan = []
        index=28+opt_header_length
        for i in range(0, frame_count):
            if_pan.append(struct.unpack('<h', msg[index+2*i:index+2*i+2]))
        if packets%20 == 0:
            print "IFPan", frame_count, ", min", min(if_pan), "max ", max(if_pan)
            #here comes a hack to set the level ragen according to the actual signal situation
            #eb500.send_cmd('stat:ext:data #219564L000009:0:0 '+str(min(if_pan[0])-30))
            #eb500.send_cmd('stat:ext:data #218563L000008:0:0 '+str(max(if_pan[0])+80))
    elif tag == 901:  # IFPan
        frame_count, reserved, opt_header_length, selector_flags = struct.unpack('!HcBL', msg[20:28])
        #print "frames: ", frame_count
        if opt_header_length != 0:
            #print "opt header length: ", opt_header_length, "msg length: ", len(msg)
            opt_header = struct.unpack('<hhLLLHhHh8sQL4sQh', msg[28:28+opt_header_length])
            #print "opt header: ", opt_header
        # now we have the values
        iq_file.write(msg[28+opt_header_length:])
        if packets%200 == 0:
            print 'IQ data' #, opt_header
    else:
        print "ignored frame, tag: ", tag

# initializations
eb200_magic = 0
eb200_sequence = -1
packets = 1
lost = 0
old_header = (0,0,0,0,0,0,0,0,0)

# open command channel
eb500=Eb500Cmd(EB500_ADDR, CMD_PORT)

# open udp channel
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', UDP_PORT))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

iq_file = False

cmd_str = ''
for arg in sys.argv:
    if arg == 'au':
        cmd_str += ',AUDIO'
    elif arg == 'if':
        cmd_str += ',IFPan'
    elif arg == 'iq':
        cmd_str += ',IF'    # TODO: should have a fifo warning or option
        iq_file = open('iq.raw','w')
    else:
        print "invalid argument ", arg



eb500.send_cmd('TRAC:UDP:DEL ALL')
eb500.send_cmd('TRAC:UDP:TAG \"'+OwnIP()+'\",' + UDP_PORT.__str__() + cmd_str)
eb500.send_cmd('TRAC:UDP:FLAG \"'+OwnIP()+'\",' + UDP_PORT.__str__() + ',\"OPT\",\"SWAP\"')

eb500.send_cmd('SYST:AUD:REM:MODE 1')
eb500.send_cmd('SYST:IF:REM:MODE SHORT')

p = pyaudio.PyAudio()
audio_stream = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=32000,
                output=True)
sndfl_stream = p.open(output_device_index = 4,
                format=pyaudio.paInt16,
                channels=2,
                rate=32000,
                output=True)



try:
    while True:
        data, addr = sock.recvfrom(102400) # get large UDP packet from receiver
        parseMessage(data)

finally:
    eb500.close()
    sock.close()
    audio_stream.stop_stream()
    sndfl_stream.stop_stream()
    audio_stream.close()
    sndfl_stream.close()
    p.terminate()
    if iq_file != False:
        iq_file.close()


    print "bye bye!"