from threading import Thread
import pyscreenshot as ImageGrab
import time
#
# def sum():
#     for i  in range(100000):
#      print("Sushil")
# def man():
#     for i in range(1000000):
#      print("Chhaya")
# t1 = Thread(target=sum)
# t2 = Thread(target=man)
#
# t1.start()
# time.sleep(.1)
# t2.start()

def Takescreenshort():
    k = 0
    while True:
        time.sleep(5)
        image = ImageGrab.grab()
        im = ImageGrab.grab(bbox=(200, 10, 1600, 500))
        im = im.save(f"/home/sushil/Desktop/{k}.png")
        print("hold_user")
        k = k + 1

Takescreenshort()
Takescreenshort()
Takescreenshort()
Takescreenshort()
Takescreenshort()
Takescreenshort()
Takescreenshort()
Takescreenshort()
Takescreenshort()


