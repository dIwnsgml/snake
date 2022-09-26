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

"""def accuracy():
  with mss() as sct:
    monitor = {"top": 500, "left": 1500, "width": 500, "height": 500}
    output = "scp-{top}x{left}_{width}x{height}.png".format(**monitor)
    img = sct.grab(monitor)
    sct.shot()
    user_screen = cv2.imread('./monitor-1.png')
    apple = cv2.imread('./apple.png')
    acc = cv2.matchTemplate(user_screen, apple, cv2.TM_CCOEFF_NORMED)
    cor = np.where(acc > 0.6)
    return cor"""
keyboard.press_and_release('down')

"""print(accuracy(), accuracy()[0][0])
mouse.move(accuracy()[1][0], accuracy()[0][0])"""
mouse.move(0, 0)