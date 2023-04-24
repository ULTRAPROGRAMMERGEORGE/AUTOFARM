from time import sleep
from threading import Thread
from main import Automine
import pyautogui as pt
from pynput.keyboard import Key, Listener, KeyCode


def proga():
    while True:
        a = Automine()
        sleep(4)
        a.nav_to_image('game.png', clicks=2)
        duration = 10
        while a.locate_hunger():
            a.move_to_food('shift',10)
        a.move_to_food('shift',10,actiton='eating')

proga()


def print_key(key):
    if hasattr(key, 'char'):
        if key.char == 'q' or key.char == 'й':
            pt.keyDown('F2')
            pt.keyUp('F2')


with Listener(on_press=print_key) as listener:
    listener.join()
