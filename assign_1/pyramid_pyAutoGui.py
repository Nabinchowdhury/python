import pyautogui
import time
def printAstericks(n):
    for i in range (0, n):
        stars = ''
        for j in range(i+1):
            stars += '*'
        pyautogui.write(stars, interval= 0.25)
        pyautogui.press('enter')

s = int(input()) 
time.sleep(5)
printAstericks(s)