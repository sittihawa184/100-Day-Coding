import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Sitti Hawa ListBox")
window.geometry('600x300')

#Membuat ListBox
ListB =Listbox(window)
ListB.insert(1, "Python")
ListB.insert(2, "PHP")
ListB.insert(3, "JAVA")
ListB.insert(4, "C")
ListB.insert(5, "C++")

ListB.pack()

window.mainloop()

