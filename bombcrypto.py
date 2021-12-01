import pyautogui
from pyautogui import locateCenterOnScreen
from time import sleep as slp
from python_imagesearch.imagesearch import imagesearch, imagesearch_loop
#


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
    pyautogui.click(972, 793)
    slp(1.2)
    pyautogui.click()
    slp(1.2)


def work(y = 443, i = 5):
    if i > 0:
        i -= 1
        slp(0.5)
        pyautogui.moveTo(894,y)
        slp(0.1)
        pyautogui.click()
        y = y + 72
        return work(y,i)
    else:
        return 0


def drag():
    slp(1)
    pyautogui.dragTo(894, 443,1, button='left',)
    slp(1)

def connect_to_wallet():
    pos = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\connect to wallet.png',1)
    slp(1)
    pyautogui.click(x=pos[0], y=pos[1])
    pos = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\assinar.png', 1)
    slp(1)
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.click()
    pos = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\treasure hunt.png',1)
    slp(0.2)
    pyautogui.click(x=pos[0], y=pos[1])
    slp(1)


def login_time_expired():
    slp(5)
    pos = imagesearch(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\login time expired.png')
    if pos != [-1,-1]:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.move(150, 145)
        pyautogui.click()
    else:
        return False




# x = 1025 y = 364


while True:
    slp(3)
    pos = imagesearch(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\erro.png')
    if pos != [-1,-1]:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.move(22, 130)
        pyautogui.click()

        connect_to_wallet()
        if login_time_expired() == False:
            pyautogui.click(x = 987, y = 555)
            open_heroes()
            for i in range(3):
                work()
                drag()
            slp(1)
            pyautogui.click(x = 1025, y = 364)





        else:
            connect_to_wallet()
            pyautogui.click(x = 987, y = 555)
            open_heroes()
            for i in range(3):
                work()
                drag()

            slp(1)
            pyautogui.click(x = 1025, y = 364)
            slp(1)
            pyautogui.click()
        slp(3600)


    else:
        open_heroes()
        for i in range(2):
            work()
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








