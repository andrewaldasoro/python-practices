import time
import pyautogui
from selenium import webdriver
import clipboard

time.sleep(15)
while True:
    time.sleep(3)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    for x in range(0, 7):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    pyautogui.hotkey('f5')
    time.sleep(4)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(3)

    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click()
    for y in range(0, 8):
        pyautogui.hotkey('down')

    for z in range(0, 7):
        pyautogui.hotkey('up')