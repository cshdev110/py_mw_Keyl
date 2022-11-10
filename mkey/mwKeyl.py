#!/usr/bin/env python

from pynput import keyboard

def on_key_press(key):
    print(key)

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
