
from tkinter import *
# import tkinter

window = Tk()

window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')  #Холст создали

canvas.pack()   #Поставили холст на мальберт

# canvas.create_rectangle(100,100,350,350,fill='black', outline='')

# canvas.create_rectangle(100,100,120,120, fill='white', outline='orange')
# canvas.create_rectangle(130,130,170,170, fill='white', outline='blue')
# canvas.create_rectangle(180,180,240,240, fill='white', outline='green')
#
# canvas.create_polygon(10, 50, 50, 10, 90, 50, fill='yellow', outline='')

canvas.create_polygon(10, 260, 60, 200, 110, 260, fill='green', outline='black')
canvas.create_rectangle(20,260,100,360, fill='orange', outline='green')

window.mainloop()





