#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

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

class CallButton(MyButton):
    def __init__(self, func, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.func = func

    def clicked(self):
        self.func()



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

class MessageBoxFactory():
    def askokcancel(title='askokcancel', message='message'):
        return lambda t=title, m=message: messagebox.askokcancel(t, m)

    def askquestion(title='askquestion', message='message'):
        return lambda t=title, m=message: messagebox.askquestion(t, m)

    def askretrycancel(title='askretrycancel', message='message'):
        return lambda t=title, m=message: messagebox.askretrycancel(t, m)

    def askyesno(title='askyesno', message='message'):
        return lambda t=title, m=message: messagebox.askyesno(t, m)

    def showerror(title='showerror', message='message'):
        return lambda t=title, m=message: messagebox.showerror(t, m)

    def showinfo(title='showinfo', message='message'):
        return lambda t=title, m=message: messagebox.showinfo(t, m)

    def showwarning(title='showwarning', message='message'):
        return lambda t=title, m=message: messagebox.showwarning(t, m)

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

class MyPanedwindow(ttk.Panedwindow):
    def __init__(self, root, title,  *args, **kwargs):
        super().__init__(master=root, *args, **kwargs)
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

        # ----------------
        # --- Nested frame
        self.f2 = MyPanedwindow(root, title='Frame Two', orient=VERTICAL)
        self.f2.add_to_notebook(self.nb)
        nf1 = ttk.Labelframe(self.f2, text="Nested Frame 1", height=30, width=100)
        nf2 = ttk.Labelframe(self.f2, text="Nested Frame 2", width=100)
        nf3 = ttk.Labelframe(self.f2, text="Nested Frame 3", width=100)
        self.f2.add(nf1)
        self.f2.add(nf2)
        self.f2.add(nf3)

        # ----------------------
        # --- MessageBox buttons
        self.f3 = MyFrame(root, title="Frame Three")
        self.f3.add_to_notebook(self.nb)
        self.b3_1 = CallButton(master=self.f3, title='askokcancel', row=0, column=0, func=MessageBoxFactory.askokcancel())
        self.b3_2 = CallButton(master=self.f3, title='askquestion', row=0, column=1, func=MessageBoxFactory.askquestion())
        self.b3_3 = CallButton(master=self.f3, title='askretrycancel', row=0, column=2, func=MessageBoxFactory.askretrycancel())
        self.b3_4 = CallButton(master=self.f3, title='askyesno', row=1, column=0, func=MessageBoxFactory.askyesno())
        self.b3_5 = CallButton(master=self.f3, title='showerror', row=1, column=1, func=MessageBoxFactory.showerror())
        self.b3_6 = CallButton(master=self.f3, title='showinfo', row=1, column=2, func=MessageBoxFactory.showinfo())
        self.b3_7 = CallButton(master=self.f3, title='showwarning', row=2, column=0, func=MessageBoxFactory.showwarning())

        # --------------------------------------
        # --- implement a regular expression GUI
        self.f4 = MyFrame(root, title="Frame Four")
        self.f4.add_to_notebook(self.nb)

        expression = StringVar()
        pattern = StringVar()
        match = StringVar()

        def get_match(*args):
            match.set(re.search(pattern.get(), expression.get()).group())

        ttk.Entry(self.f4, width=20, textvariable=expression).grid(column=0, row=0, pady=5)
        ttk.Label(self.f4, text='expression').grid(column=1, row=0, sticky=W, padx=5)

        ttk.Entry(self.f4, width=20, textvariable=pattern).grid(column=0, row=1, pady=5)
        ttk.Label(self.f4, text='pattern').grid(column=1, row=1, sticky=W, padx=5)

        ttk.Label(self.f4, textvariable=match).grid(column=0, row=2, sticky=W, padx=5)

        CallButton(master=self.f4, title="Do It", column=0, row=3, padx=5, func=get_match)

        root.mainloop()

MyApp()
