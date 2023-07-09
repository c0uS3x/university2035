from tkinter import *

window = Tk()

window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')

canvas.pack()

class triangle:
    def __init__(self, coord1, coord2, coord3):
        self.coord1 = coord1
        self.coord2 = coord2
        self.coord3 = coord3

    def create_triangle(self):
        canvas.create_polygon(self.coord1, self.coord2, self.coord3, fill='white', outline='black')

class rectangle:
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def create_rectangle(self):
        canvas.create_polygon(self.coord1, self.coord2, fill='white', outline='black')


window.mainloop()