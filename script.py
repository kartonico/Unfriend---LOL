import pyautogui as pg
import time

def icone():
    pg.moveTo(1190,345)
    pg.click(button='right')

def excluindo():
    pg.moveTo(1241,521)
    pg.click(button='left')

def excluir():

    pg.keyDown('enter')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.keyUp('enter')
