import time
import keyboard
import numpy as np
import pyautogui
import win32api
import win32con

time.sleep(2)
print("begin")

keyList = {'r'}

for c in keyList:
    pyautogui.keyDown(c)

print("keys pressed")

while not keyboard.is_pressed('q'):
    pass

print("termination asked")

for c in keyList:
    pyautogui.keyUp(c)

print("keys unpressed")
