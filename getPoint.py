import mouse
import pyautogui
import time
def getPoint(title):
    print('다음 버튼을 클릭하세요', title)
    while True:
        if mouse.is_pressed(button='left'):
            x, y = pyautogui.position()
            time.sleep(0.1)
            print(title, x, y)
            return (x, y)

getPoint('')