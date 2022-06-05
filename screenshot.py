import os
import sys
import pyautogui as pag

def screen_shot(x,y,dx,dy):
    screenshot = pag.screenshot(region=(x,y,dx,dy))
    screenshot.save('screenshot.png')

def screen_shot_all():
    screenshot = pag.screenshot()
    screenshot.save('screenshot.png')
    
if __name__ == '__main__':
    args = sys.argv
    if len(args) == 5:
        screen_shot(args[1],args[2],args[3],args[4])
    else:
        screen_shot_all()
    sys.exit(0)