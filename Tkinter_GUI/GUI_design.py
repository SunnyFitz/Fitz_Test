# !/usr/bin/env python
# -*- encoding:utf-8 -*-

import tkinter as tk

A = ''

class App:


    def __init__(self,root):
        frame = tk.Frame(root)
        frame.pack()

        #创建标签
        self.Label = tk.Label(frame , text = '强强是一个智障吗' , pady = 30)
        self.Label.pack(side = tk.TOP)

        #创建按钮
        self.hi_there1 = tk.Button(frame,text = '是的', fg = 'red' , bg = 'white' , command = self.answer_1)
        self.hi_there1.pack(side = tk.LEFT , padx = 20 , pady = 10)
        self.hi_there2 = tk.Button(frame, text='肯定是的', fg='red', bg='white', command=self.answer_2)
        self.hi_there2.pack(side=tk.RIGHT , padx = 20 , pady = 10)
        #self.hi_there2 = tk.Button(frame, text='退出', fg='red', bg='red', command=self.exit)
        #self.hi_there2.pack(side=tk.TOTTOM , padx = 20 , pady = 10)
        self.Label = tk.Label(frame, text= A , pady=30)



    #按钮的功能函数
    def answer_1(self):
        global  A
        A = '当然，强强是个ZZ！！！'
        print(A)
    def answer_2(self):
        global A
        A = '强强？那必须是个ZZ！！'
        print(A)

root = tk.Tk()
app = App(root)
root.mainloop()