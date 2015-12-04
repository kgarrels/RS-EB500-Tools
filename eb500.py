#
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

EB500_ADDR = '192.168.2.5'
CMD_PORT = 5555
UDP_PORT = 19200

__kai_debug__ = False

class Eb500Cmd (telnetlib.Telnet):
    def __init__(self, host=None, port=0):
        self = telnetlib.Telnet.__init__(self,host, port)

    def send_cmd(self, cmd):
        print "> "+ cmd
        self.write(cmd+"\n")
        ans = self.read_eager()     # FIXME: does not receive anything
        print "< " + ans
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
    global eb200_magic, eb200_sequence

    # decode eb200 header
#    magic, ver_min, ver_maj, seq_low, seq_high, data_Size =  struct.unpack('!LHHHHL', msg[0:16])     # eb200 header
#    if (eb200_magic == 0) & (magic == 0x0EB200):
#        print "received 1st EB200 frame, version ",ver_maj,".",ver_min
#        eb200_magic=magic

    # decode generic attribute
    tag, length = struct.unpack('!HH', msg[16:20])          # generic attribute, we need the tag

    # decode attribute according to tag
    if tag == 401:  # audio
        frame_count, reserved, opt_header_length, selector_flags = struct.unpack('!HcBL', msg[20:28])
#        if opt_header_length != 0:
#            print "opt header length: ", opt_header_length
#            opt_header = struct.unpack('<hhLLH8sL6sQh', msg[28:28+opt_header_length])
#            print "opt header: ", opt_header

        # outout, assume audio mode 1
        stream.write(msg[48+opt_header_length:])
    else:
        print "ignored frame, tag: ", tag

# initializations
eb200_magic = 0
eb200_sequence = -1

# open command channel
eb500=Eb500Cmd(EB500_ADDR, CMD_PORT)

# open udp channel
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', UDP_PORT))

#eb500.send_cmd('TRACE:UDP:DEL ALL')
eb500.send_cmd('TRACE:UDP:TAG:ON \''+OwnIP()+'\',' + UDP_PORT.__str__() + ',MSC,AUDIO')
eb500.send_cmd('TRACE:UDP:FLAG:ON \''+OwnIP()+'\',' + UDP_PORT.__str__() + ',\'VOLT:AC\', \'FREQ:OFFS\', \'FREQ:RX\', \'OPT\',\'SWAP\'')    #,\'SWAP\'

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=32000,
                output=True)
try:
    while True:
        data, addr = sock.recvfrom(102400) # buffer size is 1024 bytes
        # print "received message, len:", len(data), " from: ", addr
        parseMessage(data)
finally:
    eb500.close()
    sock.close()
    stream.stop_stream()
    stream.close()
    p.terminate()

    print "bye bye!"