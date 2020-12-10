#!/usr/bin/python

from pynput.mouse import Listener
from playsound import playsound
import sys, getopt

defaultSoundfile="sound/soundfile.mp3"

def on_click(x, y, button, pressed):
    if pressed:
        print("pression touche")
        playsound(defaultSoundfile)


def main():
    # Lancement du service
    with Listener(on_click=on_click) as listener:
        listener.join()
    

if __name__ == "__main__":
    main()