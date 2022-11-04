import tkinter

window = tkinter.Tk ()
window.title("Sitti_Hawa")
window.geometry('600x300')

#creating a function called say hallo
def say_hello():
    tkinter.Label(window, text="Merhaba").pack()
tkinter.Button (window, text="Click Me", Slide = "left", command = say_hello).pack()

window.mainloop()
