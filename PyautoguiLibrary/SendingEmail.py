import pyautogui as mouse
import pyautogui as time
import pyautogui as teclado
import webbrowser
# ENTRANDO NO EMAIL
webbrowser.open("https://www.google.com/")
time.sleep(5)
teclado.typewrite('mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
teclado.press('enter')
time.sleep(2)
mouse.click(x=1614, y=323)
time.sleep(3)
mouse.click(x=1400, y=169)
time.sleep(3)
#DESTINATARIO OU DESTINATARIOS COM FOR
for i in range(5):
    teclado.typewrite('RAFAEL@GAMIL.COM',interval=0.1)
    teclado.press('enter')
time.sleep(2)
mouse.click(x=2278, y=726)
time.sleep(2)
mouse.click(x=2190, y=372)
time.sleep(2)
teclado.typewrite('REUNIÃO AS 7:00',interval=0.1)
time.sleep(2)
mouse.click(x=2172, y=423)
teclado.typewrite('ALGO A ACRESSENTAR',interval=0.1)
time.sleep(2)
mouse.click(x=2192, y=737)



