from tkinter import *
from tkinter import messagebox
# Pentru a instala biblioteca folositi ### pip3 install tk ###
afisaj = Tk()
afisaj.geometry("350x350")
afisaj.title("Test")
Label(afisaj,text="Nume").grid(row=0)
Label(afisaj,text="Prenume").grid(row=1)
nume = Entry(afisaj)
prenume = Entry(afisaj)

nume.grid(row=0, column=1)
prenume.grid(row=1, column=1)

def afiseazanume():
 nume_afisaj = nume.get()
 prenume_afisaj = prenume.get()
 messagebox.showinfo("Numele", f"Salut, {nume_afisaj} {prenume_afisaj}")

Button(afisaj,text="salut", command=afiseazanume).grid(row=2)

mainloop()

