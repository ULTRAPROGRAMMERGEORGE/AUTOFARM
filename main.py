import pyautogui as pt
from time import sleep
import sys
from threading import Thread
from pynput.keyboard import Key, Listener


class Automine:

    def nav_to_image(self, image, clicks, off_x=0, off_y=0):
        position = pt.locateCenterOnScreen(image, confidence=.3)
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.2)

    def move_to_food(self, key_press, duration, actiton='attack'):
        pt.keyDown(key_press)
        if actiton == 'eating':
            print('хаваю')
            pt.keyDown('5')
            pt.keyUp('5')
            pt.keyDown('c')
            sleep(duration)
            pt.keyUp('c')
            pt.keyDown('1')
            pt.keyUp('1')
        elif actiton == 'attack':
            while duration != 0:
                print('убиваю')
                pt.keyDown('x')
                pt.keyUp('x')
                sleep(2)
                duration -= 1

    def locate_hunger(self):
            position = pt.locateCenterOnScreen('full.png')
            if position is None:
                return True
            else:
                return False
