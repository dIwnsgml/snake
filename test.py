from fileinput import filename
from PIL import ImageGrab, Image
import cv2
import numpy as np
import time
from mss import mss
from tkinter import *
import pyautogui as pag
import keyboard
import mouse
from numba import jit, cuda
import numba
from timeit import default_timer as timer
import threading
from multiprocessing.pool import ThreadPool


# To run on CPU
'''def func(a):
    for i in range(10000000):
        a[i]+= 1
# To run on GPU
@jit
def func2(x):
    return x+1
if __name__=="__main__":
    n = 10000000
    a = np.ones(n, dtype = np.float64)
    start = timer()
    func(a)
    print("without GPU:", timer()-start)
    start = timer()
    func2(a)
    numba.cuda.profile_stop()
    print("with GPU:", timer()-start)'''

def search_apple(x, y):
  start = time.time()
  with mss() as sct:
    #monitor = {"top": y, "left": x, "width": 660, "height": 600}
    #user_screen = sct.grab(monitor)
    sct.shot()
    user_screen = cv2.imread('./monitor-1.png')
    user_screen = user_screen[y:y+600, x:x+660]
    #cv2.imshow('d',user_screen)
    apple = cv2.imread('./app3.png')
    acc = cv2.matchTemplate(user_screen, apple, cv2.TM_CCOEFF_NORMED)
    cor = np.where(acc > 0.92)
    cor = cor[1][0], cor[0][0]
    return cor

t = [0, 0]
timer1 = time.time()
t[0] = threading.Thread(target = search_apple, args = (1578, 519))
t[1] = threading.Thread(target = search_apple, args = (1578, 519))
t[0].start()
t[1].start()

print(f"{time.time() - timer1:.4f}")
t[0].join()
t[1].join()
print(f"{time.time() - timer1:.4f}")

'''timer2 = time.time()
a = search_apple(1578, 519)
b = search_apple(1578, 519)
print(f"{time.time() - timer2:.4f}", a, b)'''


"""print(accuracy(), accuracy()[0][0])
mouse.move(accuracy()[1][0], accuracy()[0][0])"""


#Thread pool
timer3 = time.time()
pool = ThreadPool(processes=1)

cor1 = pool.apply_async(search_apple, (1578, 519))
cor2 = pool.apply_async(search_apple, (1578, 519))
cor3 = pool.apply_async(search_apple, (1578, 519))

returned1 = cor1.get()
returned2 = cor1.get()
returned3 = cor1.get()
print(f"{time.time() - timer3:.4}",returned1, returned2, returned3)
#mouse.move(0, 0)