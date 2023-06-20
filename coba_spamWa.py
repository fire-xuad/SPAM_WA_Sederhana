import pyautogui
import time

pyautogui.moveTo(1122,1023)
pyautogui.click()

for i in range(100):
    pyautogui.write("Test SPAM")
    time.sleep(0.2)
    pyautogui.press("Enter")