import pyautogui
import time
time.sleep(4)
count = 0
while count <=500:
    pyautogui.typewrite("Hi Mama")
    pyautogui.press("enter")
    count=count+1