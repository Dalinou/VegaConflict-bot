import time

import keyboard
import numpy as np
import pyautogui
import win32api
import win32con

time.sleep(5)
# code of Mihael Hajnic from https://github.com/mhajnic1/VegaConflict-bot


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# il serait difficile d'arrêter le programme étant donné que la souris bouge tout le temps
while not keyboard.is_pressed('q'):
    # SÉLECTIONNER LA FLOTTE À UTILISER - nous sélectionnons d'abord la flotte aléatoire, puis la principale pour que
    # la fenêtre contextuelle soit toujours active
    pyautogui.keyDown('1')
    time.sleep(np.random.uniform(0.1, 0.3))
    pyautogui.keyUp('1')

    pyautogui.keyDown('3')
    time.sleep(np.random.uniform(0.2, 0.4))
    pyautogui.keyUp('3')

    # attendre entre les minuteries, c'est pour que le jeu ne comprenne pas qu'il s'agit d'un script
    time.sleep(np.random.uniform(0.75, 1.25))

    # CHECK - est la flotte au combat
    if pyautogui.pixel(817, 1010)[0] != 232:

        # SPÉCIFIQUE À L'ÉVÉNEMENT - vérifier la fenêtre contextuelle blitz 1436 Y : 188
        # if pyautogui.locateOnScreen('blitz.png', grayscale=True, confidence=0.8) is not None:
            # désactive la fenêtre contextuelle
            # click(1436, 188)

        # vérifier si nous attaquons accidentellement avec la mauvaise flotte X : 1056 Y : 664
        if pyautogui.locateOnScreen('alert.png', grayscale=True, confidence=0.7) is not None:
            # désactive la fenêtre contextuelle
            click(1056, 664)

        # RÉPARATION GRATUITE - vérifier
        # if pyautogui.locateOnScreen('repair.png', grayscale = True, confidence = 0.8) is not None:
        # RÉPARATION GRATUITE DISPONIBLE
        # clic(978, 928)

        time.sleep(np.random.uniform(1, 2))

        # Cliquez sur trouver la flotte pour attaquer
        click(1627, 94)

        # random wait
        time.sleep(np.random.uniform(1, 1.5))

        # VÉRIFICATION DE LA COULEUR DES PIXELS DU BOUTON D'ATTAQUE
        if pyautogui.pixel(817, 1010)[0] == 232:
            # Bouton ROUGE ET PRÊT À ATTAQUER
            click(817, 1010)
            time.sleep(np.random.uniform(13, 15))
