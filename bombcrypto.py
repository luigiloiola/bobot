import pyautogui
from pyautogui import locateCenterOnScreen
from time import sleep as slp
from python_imagesearch.imagesearch import imagesearch, imagesearch_loop
import os
import shutil




# try:
#     while True:
#         x, y = pyautogui.position()
#         position = f'x:{x}  //  y:{y}'
#         print(position)
#         slp(2)
# except:
#     pass


def open_heroes():
    slp(3)  # 3600 = 1
    pos = imagesearch_loop(r'C:\bombcrypto\images\settings.png',1)
    pyautogui.moveTo(pos[0],pos[1])
    pyautogui.move(-428, 562)
    pyautogui.click()
    slp(1.2)
    pyautogui.click()
    slp(1.2)


def work(y, i=5):
    if i > 0:
        i -= 1
        slp(0.5)
        pyautogui.moveTo(894, y)
        slp(0.1)
        pyautogui.click()
        y = y + 72
        return work(y, i)
    else:
        return 0


def drag():
    slp(1)
    pyautogui.dragTo(894, imagesearch_loop(r'C:\bombcrypto\images\work button.png',1)[1],4, button='left',)
    slp(1)

def connect_to_wallet():
    pos = imagesearch_loop(r'C:\bombcrypto\images\connect to wallet.png',1)
    slp(1)
    pyautogui.click(x=pos[0], y=pos[1])
    pos = imagesearch_loop(r'C:\bombcrypto\images\assinar.png', 1)
    slp(1)
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.click()
    pos = imagesearch_loop(r'C:\bombcrypto\images\treasure hunt.png',1)
    slp(0.2)
    pyautogui.click(x=pos[0], y=pos[1])
    slp(1)


def login_time_expired():
    slp(5)
    pos = imagesearch(r'C:\bombcrypto\images\login time expired.png')
    if pos != [-1,-1]:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.move(150, 145)
        pyautogui.click()
    else:
        return False



try:
    os.mkdir(r'C:\bombcrypto')
    os.mkdir(r'C:\bombcrypto\images')
except:
    print(r'C:\bombcrypto\images already exists')


while True:
    work_y = imagesearch_loop(r'C:\bombcrypto\images\work button.png', 1)[1]

    slp(3)
    pos = imagesearch(r'C:\bombcrypto\images\erro.png')
    if pos == [-1,-1]:
        open_heroes()
        for i in range(2):
            work(work_y)
            drag()

        slp(1)
        pyautogui.click(x=1025, y=364)
        slp(1)
        pyautogui.click()
        # pos = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\x.png',1)
        # # slp(2.5)
        # # pyautogui.click(pos[0],pos[1])
        # slp(2)
        # pyautogui.click(973, 733)
        # slp(3600)
        slp(3600)


    else:
        print('tela de erro')
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.move(22, 130)
        pyautogui.click()

        connect_to_wallet()
        if login_time_expired() == False:
            pyautogui.click(x=987, y=555)
            open_heroes()
            for i in range(3):
                work(work_y)
                drag()
            slp(1)
            pyautogui.click(x=1025, y=364)
            slp(1)
            pyautogui.click()
            slp(3600)





        else:
            connect_to_wallet()
            pyautogui.click(x=987, y=555)
            open_heroes()
            for i in range(3):
                work(work_y)
                drag()

            slp(1)
            pyautogui.click(x=1025, y=364)
            slp(1)
            pyautogui.click()
        slp(3600)
