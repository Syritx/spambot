import time
import pyautogui
import random

text = ["a","b","c"]
time.sleep(2)

for i in range(20):

    pyautogui.typewrite(random.choice(text))
    pyautogui.press('enter')
    time.sleep(.5)

    print(str(i+1))