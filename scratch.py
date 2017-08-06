import telnetlib
import kivy
kivy.require('1.0.8')

from kivy.core.window import Window
from kivy.uix.widget import Widget


class Eb500Cmd (telnetlib.Telnet):
    def __init__(self, host=None, port=0):
        self = telnetlib.Telnet.__init__(self,host, port)

    def send_cmd(self, cmd):
        print "> "+ cmd
        self.write(cmd+"\n")
        #ans = self.read_until(match='', timeout=0.1)     # FIXME: does not receive anything
        #print "< " + ans
        #return ans





class MyKeyboardListener(Widget):

    def __init__(self, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('Key: ', keycode)
        print('- text is %r' % text)
        print('- modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()
        elif keycode[1] == 'left':
            eb500.send_cmd('FREQ:DEM DOWN')
        elif keycode[1] == 'right':
            eb500.send_cmd('FREQ:DEM UP')

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True


if __name__ == '__main__':
    EB500_ADDR = '192.168.2.5'
    LOCALHOST = '127.0.0.1'
    CMD_PORT = 5555
    UDP_PORT = 19000
    VRT_PORT = 4991
    TCP_PORT = 5565
    IQ_PORT = 5557

    eb500 = Eb500Cmd(EB500_ADDR, CMD_PORT)
    eb500.send_cmd('FREQ?')

    from kivy.base import runTouchApp
    runTouchApp(MyKeyboardListener())