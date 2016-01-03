#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

class MyButton(Button):
    def __init__(self, title, column, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text = title, command = self.clicked)
        self.grid(column=column, row=row, padx=5, pady=5)
        self.bind("<Return>", lambda e: self.clicked())

    def clicked(self):
        raise NotImplemented

class TrickButton(MyButton):
    def __init__(self, title, *args, **kwargs):
        super().__init__(title=title, *args, **kwargs)
        self.original_title = title
        self.alternative_title = 'hahaha'
        self.configure(width = max(len(title), len(self.alternative_title)) + 1)

    def clicked(self):
        if(self['text'] == self.original_title):
            self.configure(text=self.alternative_title)
        else:
            self.configure(text=self.original_title)

class PrintButton(MyButton):
    # TODO at seemingly random times, these buttons print twice, why?
    def __init__(self, text, *args, **kwargs):
        self.text = text
        super().__init__(*args, **kwargs)

    def clicked(self):
        print(self.text)

class ExitButton(MyButton):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.focus_force()

    def clicked(self):
        self.root.destroy()

class MyNotebook(ttk.Notebook):
    def __init__(self, root, *args, **kwargs):
        super().__init__(master=root, *args, **kwargs)
        self.grid(column=0, row=0, sticky=(N, W, E, S))

class MyFrame(ttk.Frame):
    def __init__(self, root, title,  *args, **kwargs):
        super().__init__(master=root, *args, **kwargs)
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.title=title

    def add_to_notebook(self, nb):
        nb.add(self, text=self.title)


class MyApp:
    def __init__(self):
        root = Tk()
        root.title('Test of an app')
        self.nb = MyNotebook(root)

        self.f1 = MyFrame(root, title="Frame One")
        self.f1.add_to_notebook(self.nb)
        self.pbut1 = PrintButton(text='1', master=self.f1, title='print 1', row=0, column=0)
        self.pbut2 = PrintButton(text='2', master=self.f1, title='print 2', row=0, column=1)
        self.button1 = TrickButton(master=self.f1, title='click me', row=1, column=0)
        self.button_exit = ExitButton(root, master=self.f1, title='exit', row=1, column=1)

        self.f2 = MyFrame(root, title="Frame Two")
        self.f2.add_to_notebook(self.nb)
        # TODO, find out why this is not showing up
        self.f2_nest_frame = MyFrame(self.f2, title="Frame two child")

        self.f3 = MyFrame(root, title="Frame Three")
        self.f3.add_to_notebook(self.nb)

        self.f4 = MyFrame(root, title="Frame Four")
        self.f4.add_to_notebook(self.nb)

        root.mainloop()

MyApp()
