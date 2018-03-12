# -*-  coding:UTF-8 -*-

import time
import pyHook
import pythoncom
import threading
from tkinter import *
import pyautogui as pag

x = 1
y = 0


def speed_add():
    global x
    x += 1
    print("当前速度为： " + str(x))

def speed_sub():
    global x
    if x > 1:
        x -= 1
    else:
        x = 1
    print("当前速度为： " + str(x))

def start():
    print("程序已开始运行...")
    t1 = threading.Thread(target = Mousemove, name = 'Mousemove')
    t1.start()
    
    t2 = threading.Thread(target = Muosecontrol, name = 'Muosecontrol')
    t2.start()

def stop():
     print("程序已停止...")
     root.quit()

def onMouseEvent(event):
    global x
    global y

    if event.MessageName == "mouse left down":
        y = 1     
    if event.MessageName == "mouse left up":
        y = 0
    #print(x) 
    return True

def Mousemove():
    global y
    global x

    while 1:
        if y == 1 :
            pag.moveRel(0,x,0.01)
            time.sleep(.1)

def Muosecontrol():
    hm = pyHook.HookManager()

    hm.MouseAll = onMouseEvent
    hm.HookMouse()

    pythoncom.PumpMessages()

def gui():

    Label(root,text = "作品：外挂").grid(row = 0,column= 1)
    Label(root,text = "作者：佚名").grid(row = 1,column = 1)

    Button(root,text = "Speed +",width = 10 ,command = speed_add).grid(row = 2 ,column = 0 , sticky = W , padx = 10 ,pady = 5)
    Button(root,text = "Speed -",width = 10 ,command = speed_sub).grid(row = 2 ,column = 3 , sticky = E , padx = 10 ,pady = 5)
    Button(root,text = "开始",width = 10 ,command = start).grid(row = 3 ,column = 0 , sticky = W , padx = 10 ,pady = 5)
    Button(root,text = "停止",width = 10 ,command = stop).grid(row = 3 ,column = 3 , sticky = E , padx = 10 ,pady = 5)
    time.sleep(.1)
    mainloop()


if __name__ == "__main__" :
    root = Tk()
    gui()

