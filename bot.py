import pyautogui
import keyboard
import time

pressed = False

time_1 = time.time()
time_2 = 0

screenWidth, screenHeight = pyautogui.size()
width, height = pyautogui.screenshot().size
scWidth, scHeightRef = int(width * 0.1), int(height * 0.1)
scLeft, scTop = int(width/2 - scWidth/2), int(height/2 - scHeightRef)

scHeight = height - scTop - 2*scHeightRef

fish_count = 0

print('ready!')
keyboard.wait(';')
keyboard.press_and_release('i')
time.sleep(3)
while True:

    time_2 = time.time()
    if keyboard.is_pressed('b') == True:
        print("fish count: " + str(fish_count))
        keyboard.press_and_release('i')
        break

    bobber_found = False

    if time_2 - time_1 > 0.5:
        time_1 = time.time()
        img = pyautogui.screenshot(region=(scLeft, scTop, scWidth, scHeight))
        img_w, img_h = img.size

        for x in range(0, img_w, 2):
            if bobber_found:
                break
            for y in range(0, img_h, 2):

                r,g,b = img.getpixel((x,y))[:3]

                if r/(g+b+1) > 1.6:
                    bobber_found = True
                    break

        if bobber_found == False:
            fish_count += 1
            keyboard.press_and_release('i')
            time.sleep(1)
            keyboard.press_and_release('i')
            time.sleep(3)
        
        
    elif time_2 - time_1 > 25:
        keyboard.press_and_release('i')
        time.sleep(1)
        keyboard.press_and_release('i')
        time.sleep(3)
        time_1 = time.time()