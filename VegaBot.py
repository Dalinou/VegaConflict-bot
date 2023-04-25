import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click_center(location):
    x = int(location[0] + location[2] / 2)
    y = int(location[1] + location[3] / 2)
    click(x, y)


# Configuration :
max_fight = 10
fight = 0
fleet_number = 3
short_delay = [0.2, 0.5]
large_delay = [1, 1.5]
looping_delay = 2

time.sleep(2)
print('begin')

while not keyboard.is_pressed('q') | fleet_number == 0:
    # check if any fleet is idle
    idle = pyautogui.locateOnScreen('Image/Idle.png', confidence=0.9)
    # check if any fleet need repair
    need_reparation = pyautogui.locateOnScreen('Image/Need_reparation.png', confidence=0.9)
    if idle is not None:
        print('idle fleet detected')
        # click on fleet
        click_center(idle)
        time.sleep(np.random.uniform(large_delay[0], large_delay[1]))
        if fight < max_fight:
            # check if the Search button exist
            search = pyautogui.locateOnScreen('Image/Search.png', grayscale=True, confidence=0.8)
            if search is not None:
                # click Search button
                click_center(search)
                time.sleep(np.random.uniform(short_delay[0], short_delay[1]))
                # check if the Attack button exist
                attack = pyautogui.locateOnScreen('Image/Attack.png', confidence=0.8)
                if attack is not None:
                    # send the attack
                    click_center(attack)
                    fight += 1
                    print(fight, '° attack send')
                    time.sleep(np.random.uniform(short_delay[0], short_delay[1]))
        else:
            # check if recall button found
            recall = pyautogui.locateOnScreen('Image/Recall.png', grayscale=True, confidence=0.8)
            if recall is not None:
                click_center(recall)
                time.sleep(np.random.uniform(short_delay[0], short_delay[1]))
                fleet_number -= 1
                print(fleet_number, '° fleet left')
    elif need_reparation is not None:
        print('detect a fleet needing reparation')
        # click on fleet
        click_center(need_reparation)
        time.sleep(np.random.uniform(short_delay[0], short_delay[1]))
        # check if the reparation is free
        repair = pyautogui.locateOnScreen('Image/Repair.png', grayscale=True, confidence=0.8)
        if repair is not None:
            print('free reparation possible')
            # do the reparation
            click_center(repair)
            time.sleep(np.random.uniform(short_delay[0], short_delay[1]))
        else:
            print('no free reparation possible, sending fleet home')
            # check if recall button found
            recall = pyautogui.locateOnScreen('Image/Recall.png', grayscale=True, confidence=0.8)
            if recall is not None:
                click_center(recall)
                time.sleep(np.random.uniform(short_delay[0], short_delay[1]))
                fleet_number -= 1
                print(fleet_number, '° fleet left')
    else:
        # print('nothing detect, looping')
        time.sleep(looping_delay)
