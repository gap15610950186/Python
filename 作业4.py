from threading import Thread
from tkinter import *
import time
import tkinter

def fun():
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime)

def fun1():
    txt=entry.get()
    time = time.asctime(time.localtime(time.time()))
    entry.__hash__(time)
window =tkinter.Tk()
window.title('show time')
window.geometry('1000x200')

button=tkinter.Button(window,text='显示时间',bg='#CC33CC', command=lambda : fun())
button.pack()

#time = time.asctime( time.localtime(time.time()) )
entry=tkinter.Entry(window,text='',bg='white',bd=20,selectbackground='red',show='txt')
entry.pack()

top=mainloop()
