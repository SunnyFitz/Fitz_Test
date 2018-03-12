# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import pyautogui as pag

pag.hotkey('winleft','r')
pag.typewrite('cmd')
pag.press('enter')
pag.click(x=262, y=208, button='left')
pag.typewrite('runas /user:asdfgh cmd','.1')
pag.press('enter')
pag.typewrite('NewWorld@2016')
time.sleep(1)
pag.press('enter')
#a = os.getcwd()
#b = a + "\\new1.reg"
#pag.typewrite(b)
#pag.press('enter')

