import pyautogui
from pyautogui import locateCenterOnScreen
from time import sleep as slp
from python_imagesearch.imagesearch import imagesearch, imagesearch_loop
import os
import cv2 as cv
import numpy as np
from random import randrange







# try:
#     while True:
#         x, y = pyautogui.position()
#         position = f'x:{x}  //  y:{y}'
#         print(position)
#         slp(2)
# except:
#     pass



def bypass_captcha():
    imagesearch_loop(r'C:\bombcrypto\images\are you a robot.png',1)
    slp(0.5)
    pyautogui.screenshot('screenshott.png')
    slp(0.5)
    pyautogui.screenshot('screenshott2.png')

    img = cv.imread(r'screenshott.png', cv.IMREAD_GRAYSCALE)
    img2 = cv.imread(r'screenshott2.png', cv.IMREAD_GRAYSCALE)
    imgcor = cv.imread(r'screenshott.png', cv.IMREAD_UNCHANGED)

    diff = cv.absdiff(img, img2)
    x = []
    y = []
    for i in range(len(diff)):
        for j in range(len(diff)):
            if diff[i][j] != diff[0][0]:
                y.append(i)
                x.append(j)

    os.remove('screenshott.png')
    os.remove('screenshott2.png')
    #
    # cv.imshow('image',imgcor)
    # cv.waitKey(0)

    inicio = imagesearch(r'C:\bombcrypto\images\barrinha inicio.png')
    fim = imagesearch(r'C:\bombcrypto\images\barrinha fim.png')

    dist_total_peca = 303
    dist_target = x[0] - 799
    dist_barrinha = fim[0] - inicio[0]
    drag_dist = dist_target * dist_barrinha / dist_total_peca

    pyautogui.moveTo(inicio[0], inicio[1])
    pyautogui.drag(drag_dist + 10, 0, button='left', duration=randrange(1,3))

    slp(1)
    pos = imagesearch(r'C:\bombcrypto\images\are you a robot.png')
    if pos != [-1,-1]:
        bypass_captcha()


def open_heroes():
    slp(3)  # 3600 = 1
    pos = imagesearch_loop(r'C:\bombcrypto\images\settings.png',1)
    pyautogui.moveTo(pos[0],pos[1])
    pyautogui.move(-428, 562)
    pyautogui.click()
    slp(1.2)
    pyautogui.click()
    slp(1.2)


# botao de work --- falta print
def work(x, y, i=5):
    slp(0.5)

    if i > 0:
        i -= 1
        slp(0.5)
        pyautogui.moveTo(x, y)
        slp(0.1)
        pyautogui.click()
        y = y + 72
        return work(x,y, i)
    else:
        return 0


def drag(x):
    slp(1)
    pyautogui.dragTo(x, imagesearch_loop(r'C:\bombcrypto\images\work button.png',1)[1],4, button='left',)
    slp(1)



def connect_to_wallet():
    pos = imagesearch_loop(r'C:\bombcrypto\images\connect to wallet.png',1)
    slp(1)
    pyautogui.click(x=pos[0], y=pos[1])

    slp(10)
    pos = imagesearch(r'C:\bombcrypto\images\are you a robot.png')
    if pos != [-1,-1]:
        bypass_captcha()

    slp(2)
    pos = imagesearch_loop(r'C:\bombcrypto\images\assinar.png', 1)
    slp(2)
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

def check_for_error():
    i = 10
    while i > 0:
        pos = imagesearch(r'C:\bombcrypto\images\erro.png')
        if pos != [-1, -1]:
            i = 0
            return True
        else:
            pos = imagesearch(r'C:\bombcrypto\images\are you a robot.png')
            if pos != [-1,-1]:
                bypass_captcha()
            else:
                return False

def main():

    try:
        os.mkdir(r'C:\bombcrypto')
        os.mkdir(r'C:\bombcrypto\images')
    except:
        print(r'C:\bombcrypto\images already exists')

    while True:

        slp(3)
        pos = imagesearch(r'C:\bombcrypto\images\erro.png')
        if pos == [-1, -1]:
            open_heroes()
            for i in range(2):
                pos = imagesearch(r'C:\bombcrypto\images\x work.png')
                pyautogui.moveTo(pos[0], pos[1])
                pos = [pos[0] - 144, pos[1] + 87]
                work_y = pos[1]
                work_x = pos[0]
                work(work_x, work_y)
                drag(work_x)

            x_work = imagesearch(r'C:\bombcrypto\images\x work.png')
            slp(1)
            pyautogui.click(x=x_work[0], y=x_work[1])
            slp(1)
            pyautogui.click()
            if check_for_error() == False:
                slp(600)
            else:
                main()


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
                    pos = imagesearch(r'C:\bombcrypto\images\x work.png')
                    pyautogui.moveTo(pos[0], pos[1])
                    pos = [pos[0] - 144, pos[1] + 87]
                    work_y = pos[1]
                    work_x = pos[0]
                    work(work_x, work_y)
                    drag(work_x)
                slp(1)
                pyautogui.click(x=1025, y=364)
                slp(1)
                pyautogui.click()
                check_for_error()



            else:
                connect_to_wallet()
                pyautogui.click(x=987, y=555)
                open_heroes()
                for i in range(3):
                    pos = imagesearch(r'C:\bombcrypto\images\x work.png')
                    pyautogui.moveTo(pos[0], pos[1])
                    pos = [pos[0] - 144, pos[1] + 87]
                    work_y = pos[1]
                    work_x = pos[0]
                    work(work_x, work_y)
                    drag(work_x)

                slp(1)
                pyautogui.click(x=1025, y=364)
                slp(1)
                pyautogui.click()
                check_for_error()

if __name__ == '__main__':
    main()
