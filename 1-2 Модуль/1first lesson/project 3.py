from tkinter import*
import random

window = Tk()
window.geometry('700x500')
window.title('Кликер')
window.config(bg = 'white')

points = 0

def check():
    global points
    button.place(x=random.randint(50,550), y=random.randint(50,350))
    points +=1
    label['text'] = points
    

button = Button(text = 'Нажми меня', font = ('Arial', 20), fg = 'black', command=check)
button.place(x=200, y=300)

label = Label(text=points, font = ('Arial', 20), fg = 'black', bg='white')
label.place(x=10, y=10)





window.mainloop()
