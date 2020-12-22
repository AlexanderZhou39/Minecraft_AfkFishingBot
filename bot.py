import pyautogui
import keyboard
import time

pressed = False

time_1 = time.time()
time_2 = 0

screenWidth, screenHeight = pyautogui.size()
width, height = pyautogui.screenshot().size
# print(screenWidth, screenHeight)
# print(screenWidth/2, screenHeight/2)
keyboard.wait(';')
while True:

    time_2 = time.time()
    # keyboard.press_and_release('d')
    # time.sleep(1)
    if time_2 - time_1 > 1:
        im = pyautogui.screenshot('mine_sc.png', region=((width/2-700), (height/2-600),1400, 1200))
        # im = pyautogui.screenshot('mine_sc.png')
        # print(im.size)
        print('saved screen shot!')
        break
    if keyboard.is_pressed('t') != False:
        print('--ended program--')
        break

    # pyautogui.moveTo(screenWidth/2, screenHeight/2)

    # mouseX, mouseY = pyautogui.position()

    # if pyautogui.locateOnScreen('screenshot.png', confidence = 0.8) != None:
    #     print("I see it!")
    # print(pyautogui.pixel(mouseX, mouseY))