import pyautogui as pg
import time

print('Message flooding starts in 5 seconds.')
time.sleep(5)

for i in range(1000):
    pg.write("Why you kept lying to me always? You said, you'd come...!!!")
    time.sleep(.5)
    pg.press("Enter")
    print("total send: ", i+1)