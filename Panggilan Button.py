import tkinter

window = tkinter.Tk ()
window.title("Sitti_Hawa")
window.geometry('600x300')

#MEMBUAT BUTTON
def say_halo():
     tkinter.Label(window, text="Kita Harus Tetap Semangat").pack()
tombol1 = tkinter.Button(window, text="home", command = say_halo, bg = "grey", font="20").pack()
def informasi():
    tkinter.Label(window, text="Semangat 100 Hari Ngoding").pack()
tombol2 = tkinter.Button(window, text="informasi", command = informasi, bg = "light blue", font="20").pack()

window.mainloop()
