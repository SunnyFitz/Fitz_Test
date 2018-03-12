from tkinter import *



root = Tk()

Label(root, text="first").grid(row=0)
Label(root, text="second").grid(row=1)
v1 = StringVar()
v2 = StringVar()
e1 = Entry(root , textvariable = v1)
e2 = Entry(root,  textvariable = v2 , show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)



    #root2 = Tk()
    #Label(root2, text="first").pack(side = TOP , padx = 20 , pady = 10)


def show():
    print("作品：《%s》" % e1.get())
    print("作者：《%s》" % e2.get())
    e1.delete(0,END)
    e2.delete(0,END)

def quit():
    root.quit()



Button(root, text="sign in", width=10, command = show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="exit", width=10, command = root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
