#!/usr/bin/env python3
from tkinter import *

class ZButton(Button):
    def __init__(self, title, column, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text = title)
        self.grid(column=column, row=row)
        self.bind("<1>", self.clicked)
        self.bind("<Return>", self.clicked)

    def clicked(self, e):
        raise NotImplemented 

class MyButton(ZButton):
    def clicked(self, e):
        if(self['text'] == 'click me'): 
            self.configure(text='hahaha')
        else:
            self.configure(text='click me')

class ExitButton(ZButton):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root 
        self.focus_force()

    def clicked(self, e):
        self.root.destroy()

class MyApp:
    def __init__(self):
        root = Tk()
        root.title('Test of an app')
        self.myFrame = Frame(root)
        self.myFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.button1 = MyButton(master=self.myFrame, title='click me', row=0, column=0)
        self.button_exit = ExitButton(root, master=self.myFrame, title='exit', row=1, column=0)
        root.mainloop()

MyApp()
