import pyautogui
import keyboard
import time

pressed = False

time_1 = time.time()
time_2 = 0

screenWidth, screenHeight = pyautogui.size()
width, height = pyautogui.screenshot().size
scWidth, scHeight = int(width * 0.4), int(height * 0.4)
scLeft, scTop = int(width/2-scWidth/2), int(height/2-scHeight/2)

print('ready!')
keyboard.wait(';')
while True:

    time_2 = time.time()
    # keyboard.press_and_release('d')
    # time.sleep(1)
    if time_2 - time_1 > 0.5:
        # im = pyautogui.screenshot(region=(scLeft, scTop, scWidth, scHeight))
        if pyautogui.locateOnScreen('medium.png', region=(scLeft, scTop, scWidth, scHeight), confidence = 0.7) != None:
            print('found hook!')
        # im = pyautogui.screenshot('mine_sc.png')
        # print(im.size)
        # break
        time_1 = time.time()
    if keyboard.is_pressed('t') != False:
        print('--ended program--')
        break

    # pyautogui.moveTo(screenWidth/2, screenHeight/2)

    # mouseX, mouseY = pyautogui.position()

    # if pyautogui.locateOnScreen('screenshot.png', confidence = 0.8) != None:
    #     print("I see it!")
    # print(pyautogui.pixel(mouseX, mouseY))