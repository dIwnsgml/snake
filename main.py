from fileinput import filename
from winreg import DisableReflectionKey
from PIL import ImageGrab, Image
import cv2
import numpy as np
import time
from mss import mss
from tkinter import *
import pyautogui as pag
import keyboard
import mouse
from multiprocessing.pool import ThreadPool


root = Tk()
root.title("snake")
root.geometry("500x500")

global direction
direction = 0
def search_apple(x, y):
  with mss() as sct:
    sct.shot()
  user_screen = cv2.imread('./monitor-1.png')
  user_screen = user_screen[y:y+600, x:x+660]
  #cv2.imshow('d',user_screen)
  apple = cv2.imread('./app3.png')
  acc = cv2.matchTemplate(user_screen, apple, cv2.TM_CCOEFF_NORMED)
  cor = np.where(acc > 0.92)
  if(len(cor[0])!=0):
    cor = cor[1][0], cor[0][0]
  else:
    cor = 1000
  return cor


def change_y(pre_y, cur_y, dir):
  global direction
  if(dir == 0):
    print("dir = 0")
    if(pre_y < cur_y):
      #turn right(bottom)
      print("down")
      keyboard.press_and_release('down arrow')
      time.sleep((cur_y - pre_y) / 5.5)
      direction = 1
    elif(pre_y > cur_y):
      #turn left(up)
      print("up")
      keyboard.press_and_release('up arrow')
      time.sleep((pre_y - cur_y) / 5.5)
      direction = 3

  if(dir == 2):
    if(pre_y < cur_y):
      #turn right(bottom)
      keyboard.press_and_release('up')
      time.sleep((cur_y - pre_y) / 5.5)
      direction = 3
    elif(pre_y > cur_y):
      #turn left(up)
      keyboard.press_and_release('down')
      time.sleep((pre_y - cur_y) / 5.5)
      direction = 1

def change_x(pre_x, cur_x, dir):
  global direction
  print("dsdsdsd")
  if(dir == 1):
    print("dir = 1")
    if(pre_x < cur_x):
      #turn right(bottom)
      print("down")
      keyboard.press_and_release('right')
      time.sleep((cur_x - pre_x) / 5.5)
      direction = 0
    elif(pre_x > cur_x):
      #turn left(up)
      print("up")
      keyboard.press_and_release('left')
      time.sleep((pre_x - cur_x) / 5.5)
      direction = 3

  if(dir == 3):
    print('dir = 3')
    if(pre_x < cur_x):
      #turn right(bottom)
      keyboard.press_and_release('left')
      time.sleep((cur_x - pre_x) / 5.5)
      direction = 1
    elif(pre_x > cur_x):
      #turn left(up)
      keyboard.press_and_release('right')
      time.sleep((pre_x - cur_x) / 5.5)
      direction = 0
      
def start():
  global direction
  board = loc[1][0], loc[0][0]
  mouse.move(board[0], board[1])
  mouse.click('left')
  keyboard.press_and_release('right')
  pre = [1, 1]
  for i in range(100):
    start = time.time()
    cor = search_apple(board[0], board[1])
    if(cor == 1000):
      cor = pc
    #dprint(f"{time.time() - start:.4f}", cor)
    trans_cor = round(cor[0] / 67), round(cor[1] / 66)
    if((trans_cor[0] != pre[0] or trans_cor[1] != pre[1]) and i != 0):
      #print("changed", pre, trans_cor)
      change_y(pre[1], trans_cor[1], direction)
      change_x(pre[0], trans_cor[0], direction)
      print(direction)
    print(trans_cor, pre)
    time.sleep(0.1)
    #mouse.move(cor[0] + board[0], cor[1] + board[1])
    pre = trans_cor
    pc = cor


  '''for i in range(3):
    start = time.time()
    cor = search_apple(loc[1][0], loc[0][0])
    print(cor[1][0], cor[0][0], round(cor[1][0] / 66), round(cor[0][0] / 67))
    mouse.move(cor[1][0] + loc[1][0], cor[0][0] + loc[0][0])
    print(f"{time.time()-start:.4f}")'''
  '''keyboard.press_and_release('down')
  keyboard.press_and_release('left')'''
  #print(f"{time.time() - start:.4f}")

def search():
  with mss() as sct:
    #start = time.time()
    sct.shot()
    user_screen = cv2.imread('./monitor-1.png')
    start_screen = cv2.imread('./start_screen.png')
    accuracy = cv2.matchTemplate(user_screen, start_screen, cv2.TM_CCOEFF_NORMED)
    global loc
    loc = np.where(accuracy > 0.9)
    print(loc[1][0], loc[0][0], user_screen.shape)
    


btn_search = Button(root, text="search", command = search)
btn_start = Button(root, text = "start game", command = start)

btn_search.pack()
btn_start.pack()
root.resizable(width=False, height=False)
root.mainloop()