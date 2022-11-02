import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("Hawa")
window.geometry("600x100")

#membuat pack
Button1 = Button(window, text="Left", bg="blue").pack(side=LEFT, expand=YES, fill=Y)
Button2 = Button(window, text="Top", bg="green").pack(side=TOP,expand=YES, fill=BOTH)
Button3 = Button(window, text="Right", bg="black").pack(side=LEFT, expand=YES, fill=X)
Button4 = Button(window, text="Left", bg="purple").pack(side=RIGHT, expand=YES, fill=BOTH)

window.mainloop()
