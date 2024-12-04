import tkinter as tk
import math  

def adunare():
    try:
        numar1 = float(entry1.get())
        numar2 = float(entry2.get())
        rezultat = numar1 + numar2
        label_rezultat.config(text="Rezultatul: " + str(rezultat))
    except ValueError:
        label_rezultat.config(text="Introduceti valori valide.")

def scadere():
    try:
        numar1 = float(entry1.get())
        numar2 = float(entry2.get())
        rezultat = numar1 - numar2
        label_rezultat.config(text="Rezultatul: " + str(rezultat))
    except ValueError:
        label_rezultat.config(text="Introduceti valori valide.")

def inmultire():
    try:
        numar1 = float(entry1.get())
        numar2 = float(entry2.get())
        rezultat = numar1 * numar2
        label_rezultat.config(text="Rezultatul: " + str(rezultat))
    except ValueError:
        label_rezultat.config(text="Introduceti valori valide.")

def impartire():
    try:
        numar1 = float(entry1.get())
        numar2 = float(entry2.get())
        if numar2 == 0:
            label_rezultat.config(text="Eroare: Impartire la 0!")
        else:
            rezultat = numar1 / numar2
            label_rezultat.config(text="Rezultatul: " + str(rezultat))
    except ValueError:
        label_rezultat.config(text="Introduceti valori valide.")

def ridicare_putere():
    try:
        numar1 = float(entry1.get())
        numar2 = float(entry2.get())
        rezultat = numar1 ** numar2  # Ridicare la putere
        label_rezultat.config(text="Rezultatul: " + str(rezultat))
    except ValueError:
        label_rezultat.config(text="Introduceti valori valide.")

def radical():
    try:
        numar = float(entry1.get())  # Se calculează radicalul doar pentru primul număr
        if numar < 0:
            label_rezultat.config(text="Eroare: Radicalul unui număr negativ nu este definit în numerele reale!")
        else:
            rezultat = math.sqrt(numar)  # Radicalul pătrat al numărului
            label_rezultat.config(text="Rezultatul: " + str(rezultat))
    except ValueError:
        label_rezultat.config(text="Introduceti valori valide.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_rezultat.config(text="Rezultatul: ")

root = tk.Tk()
root.title("Calculator")

label1 = tk.Label(root, text="Introduceti primul numar:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Introduceti al doilea numar:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

buton_adunare = tk.Button(root, text="Adunare", command=adunare)
buton_adunare.pack()

buton_scadere = tk.Button(root, text="Scadere", command=scadere)
buton_scadere.pack()

buton_inmultire = tk.Button(root, text="Inmultire", command=inmultire)
buton_inmultire.pack()

buton_impartire = tk.Button(root, text="Impartire", command=impartire)
buton_impartire.pack()

buton_ridicare_putere = tk.Button(root, text="Ridicare la putere", command=ridicare_putere)
buton_ridicare_putere.pack()

buton_radical = tk.Button(root, text="Radical", command=radical)
buton_radical.pack()

buton_clear = tk.Button(root, text="Stergere", command=clear)
buton_clear.pack()

label_rezultat = tk.Label(root, text="Rezultatul: ")
label_rezultat.pack()

root.mainloop()

