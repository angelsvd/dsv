import pyautogui as pag
import time
import os
import tkinter
import move
import cv2
from PIL import ImageGrab
import numpy as np
import imagesearch

cmd = """
osascript -e 'activate application "Roblox"' 
"""
os.system(cmd)

time.sleep(1)
savedata = {}
def loadSave():
    with open('save.txt') as f:
        lines = f.read().split("\n")
    f.close()
    for s in lines:
        l = s.replace(" ","").split(":")
        if l[1].isdigit():
            l[1] = int(l[1])
        savedata[l[0]] = l[1]
loadSave()

def reset():
    pag.moveTo(350,100)
    ww = savedata["ww"]
    wh = savedata["wh"]
    print(ww)
    xo = ww//4
    yo = wh//4*3
    xt = xo*3
    yt = wh
    time.sleep(2)
    pag.press('esc')
    time.sleep(0.1)
    pag.press('r')
    time.sleep(0.2)
    pag.press('enter')
    time.sleep(8)
    for _ in range(4):
        pag.press('pgup')
    time.sleep(0.1)
    for _ in range(6):
        pag.press('o')
    #im = pag.screenshot(region = (xo,yo,xt,yt))
    #im.save('a.png')

    time.sleep(0.4)
    for _ in range(4):
        r = imagesearch.find("hive1.png",0.85, xo, yo, xt, yt)
        if r:
            time.sleep(0.1)
            for _ in range(4):
                pag.press(".")

            time.sleep(0.1)
            for _ in range(4):
                pag.press('pgdn')
            break
        for _ in range(4):
            pag.press(",")
        time.sleep(0.5)
    time.sleep(1)

reset()
















'''
r = pag.locateCenterOnScreen("./images/saturator.png",confidence=0.97)
if r:
    print(r)
    pag.moveTo(r[0]//2,r[1]//2)


winup = wh / 2.14
windown = wh / 1.88
winleft = ww / 2.14
winright = wh / 1.88

winup = wh / 2
windown = wh / 2
winleft = ww / 2
winright = wh / 2



screen = np.array(ImageGrab.grab())
screen = cv2.cvtColor(src=screen, code=cv2.COLOR_BGR2RGB)

small_image = cv2.imread('./images/saturator.png')
large_image = screen
result = cv2.matchTemplate(small_image, large_image, method)
mn,_,mnLoc,_ = cv2.minMaxLoc(result)
MPx,MPy = mnLoc
print(MPx,MPy)
pag.moveTo(MPx//2,MPy//2)
# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)

# The image is only displayed if we call this
cv2.waitKey(0)


method = cv2.TM_SQDIFF_NORMED
while True:
    screen = np.array(ImageGrab.grab())
    screen = cv2.cvtColor(src=screen, code=cv2.COLOR_BGR2RGB)

    small_image = cv2.imread('./images/saturator4.png')
    large_image = screen
    result = cv2.matchTemplate(small_image, large_image, method)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    x,y = mnLoc

    print(x,y)
    print(mn)
    pag.moveTo(x//2,y//2)

    if abs(x-winleft) < 50 and abs(y-winup) < 50:
        break
    elif mn < 0.007:
        if x < winleft:
            move.hold("a",0.1)
            print("a")
        elif x > winright:
            move.hold("d",0.1)
            print("d")

        if y < winup:
            move.hold("w",0.1)
            print("w")
        elif y > windown:
            move.hold("s",0.1)
            print("s")
'''





