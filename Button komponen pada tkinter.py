#membuat button
import tkinter
from tkinter import *
syp =  tkinter.Tk()
syp.title('membuat button')
syp.geometry('200x400')

def mahasiswa():
    print("Tetap semangat :)")

btn = Button(syp, text="Merhaba", fg="#0000FF", padx=12, command=mahasiswa)
btn.pack()
syp.mainloop()
