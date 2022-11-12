import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Sitti Hawa")
window.geometry('600x300')


#Membuat SpinBox
spin = Spinbox(window, from_=0, to=50).pack()

#Membuat check button
checkB1 = Checkbutton(window, text="Perempuan").pack()

#Membuat radio button
Radiob1 = Radiobutton(window, text="UNSULBAR", value=1).pack()

#Membuat Entry
Entry1 = tkinter.Entry(window, bg="light blue", fg="black").pack()
Entry2 = tkinter.Entry(window).pack()

#Membuat Message Box
def clicked():
    messagebox.showinfo('Hawa', 'Thanks')
btn = tkinter.Button(window, text = "Click", command=clicked).pack()

window.mainloop()
