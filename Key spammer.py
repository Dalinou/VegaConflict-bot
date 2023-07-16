import time
import keyboard
import numpy as np
import pyautogui
import win32api
import win32con
from KeyBoard_key_list import VK_CODE

time.sleep(2)
print("begin")

keyList = {'2', '/'}

while not keyboard.is_pressed('q'):
    for i in keyList:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)

