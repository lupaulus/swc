import pynput;

from pynput.mouse import Listener
from playsound import playsound



def on_click(x, y, button, pressed):
    if pressed:
        print("pression touche")
        playsound("sound/soundfile.mp3")


def main():
    with Listener(on_click=on_click) as listener:
        listener.join()
    

if __name__ == "__main__":
    main()