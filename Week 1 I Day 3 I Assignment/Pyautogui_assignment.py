import pyautogui
import time
from datetime import datetime
pyautogui.FAILSAFE
pyautogui.PAUSE

print("Step 1: Open the Microsoft Edge browser...")
time.sleep (1)
pyautogui.hotkey ('win', 's')
time.sleep(1)
pyautogui.write('edge')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

print("Step 2: Go to the website...")
pyautogui.hotkey('ctrl','t', interval=0.1)
time.sleep(1)
pyautogui.write('https://meteofor.com/weather-ajman-5532/month/', interval=0.15)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

print("Step 3: Copy the fulldata of the Website...")
pyautogui.hotkey('ctrl', 'a', interval=0.1)
time.sleep(1)
pyautogui.hotkey('ctrl', 'c', interval=0.5)
time.sleep(1)

print("Step 4: Open new Notepad...")
time.sleep (1)
pyautogui.hotkey ('win', 's')
time.sleep(1)
pyautogui.write('notepad')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

print("Step 5: Paste the Data")
pyautogui.hotkey('ctrl', 'v', interval=0.1)
time.sleep(1)
pyautogui.hotkey('ctrl', 's', interval=0.1)
time.sleep(1)
pyautogui.write('daily_report_02 Oct')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)