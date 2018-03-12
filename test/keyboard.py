import time
import threading
import pyHook
import pythoncom
import pyautogui as pag


speed = 1
x = 0
#def onKeyboardEvent(event):
    
#    global speed
#    windowTitle = create_string_buffer(512)
#    windll.user32.GetWindowTextA(event.Window,byref(windowTitle),512)
#    print(event.Ascii)
#    if (event.Ascii == 16):
#        speed += 1
#        print('当前鼠标速度等级为 ' + str(speed))
#    if (event.Ascii == 12):
#        if speed <= 1:
#            speed = 1
#        else:
#            speed -= 1
#        print('当前鼠标速度等级为 ' + str(speed))
#    #print('刚刚按下了"{0}"键'.format(chr(event.Ascii)))
#    return True


def onMouseEvent(event):
    global speed
    global x

    if event.MessageName == "mouse left down":
        x = 1     
    if event.MessageName == "mouse left up":
        x = 0
    #print(x) 
    return True

def Mousemove():
    global x
    global speed

    while 1:
        if x == 1 :
            pag.moveRel(0,3,0.01)
            time.sleep(.1)

def Muosecontrol():
    hm = pyHook.HookManager()

#    hm.KeyDown = onKeyboardEvent
#    hm.HookKeyboard()

    hm.MouseAll = onMouseEvent
    hm.HookMouse()

    pythoncom.PumpMessages()


if __name__ == '__main__':
    
    t1 = threading.Thread(target = Mousemove, name = 'Mousemove')
    t1.start()
    
    t2 = threading.Thread(target = Muosecontrol, name = 'Muosecontrol')
    t2.start()
