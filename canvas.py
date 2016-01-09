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
            self.width = math.floor(max(1, self.width - 1))
        # Why? What is the significance of 4 and 5?
        if event.num == 4 or event.delta == 120:
            self.width = math.floor(min(500, self.width + 1))

    def drawPolygon(self, event):
        self.canvas.create_polygon(
            self.lastx, self.lasty - self.width/2,
            self.lastx, self.lasty + self.width/2,
            event.x, event.y + self.width/2,
            event.x, event.y - self.width/2,
            fill=self.fill)

    def addLine(self, event):
        self.fill = 'blue' if self.fill == 'red' else 'red'
        self.drawPolygon(event)
        self.xy(event)

App()
