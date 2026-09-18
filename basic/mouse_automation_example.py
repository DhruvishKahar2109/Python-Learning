import pyautogui
import time

pyautogui.hotkey("win", "r")

time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("Hello Dhruvish, Welcome to Start learning piPython!")


screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")
#
# pyautogui.moveTo(500, 300)
# pyautogui.click(500,300)
#
# pyautogui.write("Hello World")
# pyautogui.press("enter")

