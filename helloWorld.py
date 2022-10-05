from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Olá Mundo! ").grid(column=0, row=0) # Texto da tela

ttk.Button(frm, text="Sair", command=root.destroy).grid(column=1, row=0) # Botão sair com comando destroy
root.mainloop()