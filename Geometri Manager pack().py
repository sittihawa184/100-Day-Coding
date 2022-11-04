import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("Hawa")
window.geometry("600x100")

#membuat pack
Button1 = Button(window, text="Hawa", bg="light blue").pack(side=TOP, expand=YES, fill=BOTH)
Button2 = Button(window, text="WASKIA", bg="green").pack(side=TOP,expand=YES, fill=BOTH)
Button3 = Button(window, text="ARFAN", bg="yellow").pack(side=LEFT, expand=YES, fill=X)

window.mainloop()
