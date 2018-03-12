# -*- coding: utf-8 -*-

import xlrd
import easygui
import tkinter as tk
from tkinter import filedialog

def read_excel():
    pass

def compare_excel():
    pass

def choose_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path
    
if __name__ == '__main__' :
    easygui.msgbox('请在点击"OK"后选择要对比的文件')
    file1 = choose_file()
    print(file1)
