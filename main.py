from fileinput import filename
from PIL import ImageGrab, Image
import cv2
import numpy as np
import time
from mss import mss
from tkinter import *
import pyautogui as pag
import keyboard

root = Tk()
root.title("snake")
root.geometry("500x500")

def start():
  with mss() as sct:
    user_screen = sct.shot()
    user_screen = cv2.imread(user_screen)
    start_screen = cv2.imread('./start_screen.png')
    h, y = start_screen.shape[:-1]
    global loc
    for i in range(3):
      start_screen = cv2.resize(start_screen, (y, h), interpolation=cv2.INTER_AREA)
      accuracy = cv2.matchTemplate(user_screen, start_screen, cv2.TM_CCOEFF_NORMED)
      loc = np.where(accuracy > 0.9)
      h = int(h * 1.1)
      y = int(y * 1.1)
      print(loc)
    print(loc)
    keyboard.press_and_release('right')


"""with mss() as sct:
  user_screen = sct.shot()
  user_screen = cv2.imread(user_screen)
  area = cv2.imread('./area.png')
  h, y = area.shape[:-1]
  print(area.shape)
  loc = 0
  for i in range(10):
    area = cv2.resize(area, (y, h), interpolation=cv2.INTER_AREA)
    accuracy = cv2.matchTemplate(user_screen, area, cv2.TM_CCOEFF_NORMED)
    loc = np.where(accuracy > 0.9)
    #print(loc)
    h = int(h * 1.1)
    y = int(y * 1.1)"""

btn_start = Button(root, text="start", command = start)
btn_start.pack()
root.resizable(width=False, height=False)
root.mainloop()