#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
import math

class App:
    def __init__(self):
        self.lastx = 0
        self.lasty = 0
        self.fill  = 'red'
        self.width = 2

        root = Tk()
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.canvas = Canvas(root)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.canvas.bind("<Button-1>", self.xy)
        self.canvas.bind("<B1-Motion>", self.addLine)

        # with Windows
        self.canvas.bind("<MouseWheel>", self.changeWidth)
        # with Linux OS
        self.canvas.bind("<Button-4>", self.changeWidth)
        self.canvas.bind("<Button-5>", self.changeWidth)

        root.mainloop()

    def xy(self, event):
        self.lastx, self.lasty = event.x, event.y

    def changeWidth(self, event):
        # Why?
        if event.num == 5 or event.delta == -120:
            self.width = max(1, self.width - 1)
        # Why? What is the significance of 4 and 5?
        if event.num == 4 or event.delta == 120:
            self.width = min(500, self.width + 1)

    def addLine(self, event):
        if self.fill == 'red':
            self.fill = 'blue'
        else:
            self.fill = 'red'
        self.canvas.create_line(
            self.lastx, self.lasty, event.x, event.y,
            fill=self.fill, width=math.floor(self.width))
        self.lastx, self.lasty = event.x, event.y

App()
