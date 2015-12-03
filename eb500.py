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
        ans = self.read_eager() #FIXME: does not receive anything
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
    tag, length = struct.unpack('!HH', msg[16:20])
    data = msg[20:]

    if __kai_debug__:
        print "raw header:   ", StrToHex(msg[0:16])
        print "EB200 header: ", struct.unpack('!LHHHHL', msg[0:16])     #eb200 header
        print "raw gen att:  ", StrToHex(msg[16:20])
        print "tag, len:     ", tag, length
        print "data:         ", StrToHex(data)

    if tag == 401:  # audio
        #frame_count, reserved, opt_header_length, selector_flags, opt_header = struct.unpack('!HcBL42s', msg[20:70])
        #print "audio trace, frames: ", frameCount, ", opt header length: ", optHeaderLength, ", selector flags: ", selectorFlags
        stream.write(msg[70:])  #FIXME: this is maybe too simple, we rely on no header present
    else:
        print "ignored frame, tag: ", tag



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