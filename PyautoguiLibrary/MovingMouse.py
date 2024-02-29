import pyautogui as mouse
import pyautogui as time


for i in range(5):
    print(mouse.position())
    time.sleep(0.1)
for i in range(3):
    mouse.mouseUp(x=1113, y=249, duration=0.5)
    mouse.mouseUp(x=853, y=242, duration=0.5)
    mouse.mouseUp(x=863, y=392, duration=0.5)
    mouse.mouseUp(x=1151, y=383, duration=0.5)