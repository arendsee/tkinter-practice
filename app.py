#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

class ZButton(Button):
    def __init__(self, title, column, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text = title, command = self.clicked)
        self.grid(column=column, row=row, padx=5, pady=5)
        self.bind("<Return>", lambda e: self.clicked())

    def clicked(self):
        raise NotImplemented 

class MyButton(ZButton):
    def clicked(self):
        if(self['text'] == 'click me'): 
            self.configure(text='hahaha')
        else:
            self.configure(text='click me')

class PrintButton(ZButton):
    def __init__(self, text, *args, **kwargs):
        self.text = text
        super().__init__(*args, **kwargs)

    def clicked(self):
        print(self.text)

class ExitButton(ZButton):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root 
        self.focus_force()

    def clicked(self):
        self.root.destroy()

class MyApp:
    def __init__(self):
        root = Tk()
        root.title('Test of an app')
        self.nb = ttk.Notebook(root)
        self.nb.grid(column=0, row=0, sticky=(N, W, E, S))

        self.frame_1 = ttk.Frame(self.nb)
        self.frame_1.grid(column=0, row=0, sticky=(N, W, E, S))
        self.button1 = MyButton(master=self.frame_1, title='click me', row=0, column=0)
        self.button_exit = ExitButton(root, master=self.frame_1, title='exit', row=0, column=1)
        self.nb.add(self.frame_1, text='Frame One')


        
        self.frame_2 = ttk.Frame(self.nb)
        self.frame_2.grid(column=0, row=0, sticky=(N, W, E, S))
        self.pbut1 = PrintButton(text='1', master=self.frame_2, title='print 1', row=1, column=0)
        self.pbut2 = PrintButton(text='2', master=self.frame_2, title='print 2', row=1, column=2)
        self.nb.add(self.frame_2, text='Frame Two')

        root.mainloop()

MyApp()
