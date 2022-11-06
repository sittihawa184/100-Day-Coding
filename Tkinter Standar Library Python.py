import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
window=tk.Tk()
window.configure(bg="light blue")
window.geometry("300x200")
window.resizable(False, False)
window.title("Who Are You?")

NAMA_DEPAN =tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

#frame input
input_frame = ttk.Frame(window)

#penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)
#komponen komponen
#1.label nama depan
nama_depan_label = ttk.Label(input_frame, textvariable=NAMA_DEPAN)
nama_depan_label.pack(padx=10,fill="x",expand=True)

#2.label nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

#3.label nama belakang
nama_belakang_label = ttk.Label(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_label.pack(padx=10,fill="x",expand=True)

#4.label nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

#5. TOMBOL
def tombol_klik():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan=f"Merhaba {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()},Assalamualaikum"
    showinfo(title="Merhaba",message=pesan)
tombol_sapa = ttk.Button(input_frame, text="Click Here!", command=tombol_klik)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=True)

window.mainloop()
