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
from multiprocessing.pool import ThreadPool
import threading


root = Tk()
root.title("snake")
root.geometry("500x500")

def screen_shot(x, y):
  with mss() as sct:
    sct.shot()
  global user_screen
  user_screen = cv2.imread('./monitor-1.png')
  user_screen = user_screen[y:y + 600, x:x + 660]

def read_img():
  global apple
  apple = cv2.imread('./app3.png')

def search_apple(x, y):
  thr = [0, 0]
  thr[0] = threading.Thread(target = screen_shot, args = (x, y))
  thr[1] = threading.Thread(target = read_img)

  thr[0].start()
  thr[1].start()

  thr[0].join()
  thr[1].join()
  #cv2.imshow('d',user_screen)
  acc = cv2.matchTemplate(user_screen, apple, cv2.TM_CCOEFF_NORMED)
  cor = np.where(acc > 0.92)
  cor = cor[1][0], cor[0][0]
  return cor

def start():
  board = loc[1][0], loc[0][0]
  mouse.move(board[0], board[1])
  mouse.click('left')
  keyboard.press_and_release('right')
  pre = [0, 0]
  for i in range(6):
    start = time.time()
    cor = search_apple(board[0], board[1])
    print(f"{time.time() - start:.4f}")
    trans_cor = round(cor[0] / 67), round(cor[1] / 66)
    if((trans_cor[0] != pre[0] or trans_cor[1] != pre[1]) and i != 0):
      #print("changed", cor[1], cor[0], trans_cor[0], trans_cor[1], pre)
      change_y(pre[1], trans_cor[1], 0)
    #print(cor[1], cor[0], trans_cor[0], trans_cor[1], pre)
    #mouse.move(cor[0] + board[0], cor[1] + board[1])
    pre = trans_cor
    time.sleep(0.265)

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
    
def change_y(pre_y, cur_y, dir):
  if(dir == 0):
    print("dir = 0")
    if(pre_y < cur_y):
      #turn right(bottom)
      print("down")
      keyboard.press_and_release('down arrow')
      time.sleep((cur_y - pre_y) / 5.67)
      keyboard.press_and_release('left')
      return 0
    elif(pre_y > cur_y):
      #turn left(up)
      print("up")
      keyboard.press_and_release('up arrow')
      time.sleep((pre_y - cur_y) / 5.67)
      keyboard.press_and_release('left')
      return 0

  if(dir == 2):
    if(pre_y < cur_y):
      #turn right(bottom)
      keyboard.press_and_release('up')
      return 0
    elif(pre_y > cur_y):
      #turn left(up)
      keyboard.press_and_release('down')
      return 0

def change_x(pre_x, cur_x, dir):
  if(dir == 1):
    if(pre_x < cur_x):
      #turn left(right)
      keyboard.press_and_release('right')
      return 0
    elif(pre_x > cur_x):
      #turn right(left)
      keyboard.press_and_release('left')
      return 0
  elif(dir == 3):
    if(pre_x < cur_x):
      #turn right(right)
      keyboard.press_and_release('left')
      return 0
    elif(pre_x > cur_x):
      #turn left(left)
      keyboard.press_and_release('right')
      return 0



btn_search = Button(root, text="search", command = search)
btn_start = Button(root, text = "start game", command = start)

btn_search.pack()
btn_start.pack()
root.resizable(width=False, height=False)
root.mainloop()