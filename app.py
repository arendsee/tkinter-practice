#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re


class MyButton(Button):

    def __init__(self, title, column, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text=title, command=self.clicked)
        self.grid(column=column, row=row, padx=5, pady=5)
        self.bind("<Return>", lambda e: self.clicked())

    def clicked(self):
        raise NotImplemented


class TrickButton(MyButton):

    def __init__(self, title, *args, **kwargs):
        super().__init__(title=title, *args, **kwargs)
        self.original_title = title
        self.alternative_title = 'hahaha'
        self.configure(width=max(len(title), len(self.alternative_title)) + 1)

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
        self.title = title

    def add_to_notebook(self, nb):
        nb.add(self, text=self.title)


class MyPanedwindow(ttk.Panedwindow):

    def __init__(self, root, title,  *args, **kwargs):
        super().__init__(master=root, *args, **kwargs)
        self.title = title

    def add_to_notebook(self, nb):
        nb.add(self, text=self.title)


class FloatingWindow(MyFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(relief='raised', padding=(30, 20))

    def add_to_notebook(self, nb):
        NotImplemented


class Draggable:
    '''
    This (currently incomplete) class is used to add Draggability to an object.
    It takes the thing (a widget of some sort) and a canvas as arguments.
    '''

    def __init__(self, widget, canvas, *args, **kwargs):
        self.widget = widget
        self.canvas = canvas

        self.fid = canvas.create_window(window=widget, *args, **kwargs)
        widget.bind('<ButtonPress-1>',   self.select)
        widget.bind('<B1-Motion>',       self.move)
        widget.bind('<ButtonRelease-1>', self.drop)

    def move(self, event):
        dx = event.x - self.x
        dy = event.y - self.y
        self.canvas.move(self.fid, dx, dy)

    def select(self, event):
        # set initial location relative to the canvas
        self.x = self.canvas.canvasx(event.x)
        self.y = self.canvas.canvasy(event.y)

    def drop(self, event):
        NotImplemented


class MyApp:

    def __init__(self):
        self.root = Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.title('Test of an app')
        self.nb = MyNotebook(self.root)

        self.add_f1()
        self.add_f2()
        self.add_f3()
        self.add_f4()
        self.add_f5()

        self.root.mainloop()

    def add_f1(self):
        # Simple buttons
        f1 = MyFrame(self.root, title="Simple buttons")
        f1.add_to_notebook(self.nb)
        PrintButton(
            text='1',
            master=f1,
            title='print 1',
            row=0,
            column=0)
        PrintButton(
            text='2',
            master=f1,
            title='print 2',
            row=0,
            column=1)
        TrickButton(master=f1, title='click me', row=1, column=0)
        ExitButton(
            self.root,
            master=f1,
            title='exit',
            row=1,
            column=1)

    def add_f2(self):
        # Nested frame
        f2 = MyPanedwindow(self.root, title='Nested frames', orient=VERTICAL)
        f2.add_to_notebook(self.nb)
        nf1 = ttk.Labelframe(f2, text="Nested Frame 1")
        nf2 = ttk.Labelframe(f2, text="Nested Frame 2")
        nf3 = ttk.Labelframe(f2, text="Nested Frame 3")
        ttk.Label(nf1, text='frame 1').grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(nf2, text='frame 2').grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(nf3, text='frame 3').grid(row=0, column=0, padx=5, pady=5)
        f2.add(nf1)
        f2.add(nf2)
        f2.add(nf3)

    def add_f3(self):
        # MessageBox buttons
        f3 = MyFrame(self.root, title="messagebox")
        f3.add_to_notebook(self.nb)
        CallButton(
            master=f3,
            title='askokcancel',
            row=0,
            column=0,
            func=MessageBoxFactory.askokcancel())
        CallButton(
            master=f3,
            title='askquestion',
            row=0,
            column=1,
            func=MessageBoxFactory.askquestion())
        CallButton(
            master=f3,
            title='askretrycancel',
            row=0,
            column=2,
            func=MessageBoxFactory.askretrycancel())
        CallButton(
            master=f3,
            title='askyesno',
            row=1,
            column=0,
            func=MessageBoxFactory.askyesno())
        CallButton(
            master=f3,
            title='showerror',
            row=1,
            column=1,
            func=MessageBoxFactory.showerror())
        CallButton(
            master=f3,
            title='showinfo',
            row=1,
            column=2,
            func=MessageBoxFactory.showinfo())
        CallButton(
            master=f3,
            title='showwarning',
            row=2,
            column=0,
            func=MessageBoxFactory.showwarning())

    def add_f4(self):
        # implement a regular expression GUI
        f4 = MyFrame(self.root, title="regex")
        f4.add_to_notebook(self.nb)
        expression = StringVar()
        pattern = StringVar()
        match = StringVar()

        def get_match(*args):
            match.set(re.search(pattern.get(), expression.get()).group())

        ttk.Entry(
            f4,
            width=20,
            textvariable=expression).grid(
            column=0,
            row=0,
            pady=5)
        ttk.Label(f4, text='expression').grid(column=1, row=0, sticky=W, padx=5)
        ttk.Entry(
            f4,
            width=20,
            textvariable=pattern).grid(
            column=0,
            row=1,
            pady=5)
        ttk.Label(f4, text='pattern').grid(column=1, row=1, sticky=W, padx=5)
        ttk.Label(
            f4,
            textvariable=match).grid(
            column=0,
            row=2,
            sticky=W,
         padx=5)
        CallButton(
            master=f4,
            title="Do It",
            column=0,
            row=3,
            padx=5,
            func=get_match)

    def add_f5(self):
        '''
        The Canvas object is complicated and powerful. I should spend some
        time working out exactly how to work with it. Here are some nice
        tutorials:
            http://effbot.org/tkinterbook/canvas.htm - nice description,
            also specifies parameters for all canvas functions
        '''
        f5 = MyFrame(self.root, title="canvas")
        f5.add_to_notebook(self.nb)
        canvas = Canvas(f5)
        canvas.grid(column=0, row=0, sticky=(N, W, E, S))

        cf = FloatingWindow(root=f5, title="Floating Window")
        CallButton(
            master=cf,
            title='showinfo',
            row=0,
            column=0,
            func=MessageBoxFactory.showinfo())
        Draggable(cf, canvas, 50, 30)


if __name__ == '__main__':
    MyApp()
