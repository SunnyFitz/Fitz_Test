import time
import pyHook
import pythoncom
from ctypes import *
import pyautogui as pag

def onMouseEvent(event):

    print(event.MessageName)
    return True

if __name__ == '__main__':
    hm = pyHook.HookManager()


    hm.MouseAll = onMouseEvent
    hm.HookMouse()

    pythoncom.PumpMessages()
