import time
import pyautogui as pg
import pyscreenshot as ImageGrab
import PIL

image = ImageGrab.grab()
im=ImageGrab.grab(bbox=(200,50,1600,600))

im = im.save("/home/sushil/Desktop/o.png")

def Takescreenshort(hold_user):
    time.sleep(2)
    image = ImageGrab.grab()
    im = ImageGrab.grab(bbox=(200, 10, 1600, 500))
    im = im.save("/home/sushil/Desktop/o.png")
    print(hold_user)
    return hold_user

Takescreenshort(8)