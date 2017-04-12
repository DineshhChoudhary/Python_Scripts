import pyautogui
import time
import os
from time import strftime,gmtime
i=strftime("%a%d%b%Y%H%m%S",gmtime())

os.chdir("./photo")

while True:
    scrn=pyautogui.screenshot()
    scrn.save('photo'+i+'.png')
    time.sleep(300)
