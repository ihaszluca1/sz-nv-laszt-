#a szükséges beimportálások
from tkinter import *
import random
import time


#ablak létrehozása
root = Tk()
#ablak elnevezése
root.title("Színválasztó")

#háttér szín beállítása
root.config(bg="#cce3de")


#a szinek kiírása és beszínezése
def randomszin():
    colors = ["piros", "zöld", "kék", "sárga", "narancs", "lila", "barna", "fekete", "fehér"]
    sz = ["red", "green", "blue", "yellow", "orange", "magenta", "brown", "black", "white"]
    ran = random.randint(0,8)
    kiszin = colors[ran]
    entry1 = Entry(root, bg="white", width=20, font=("Arial", 12,), borderwidth=1, relief= "solid", justify="center")
    entry1.grid(column=1, row=1, columnspan=4, padx=10, pady=10)
    entry1.insert(END, kiszin)


#  dropdown megcsinálása
szamok = ["1", "2", "3", "4", "5", "6", "7", "8" ]
clicked = IntVar() 
clicked.set( "2" )
kerdes = Label(root, bg="#cce3de", text="Hány szín legyen?").grid(column=1, row=0)
drop = OptionMenu( root , clicked , *szamok ) 
drop.grid(column=2, row=0)


#
szin = Label(root, bg="#cce3de", text="")
szin.grid(column=0, row=1, columnspan=4, padx=10, pady=10)

entry = Entry(root, bg="white", width=20, font=("Times New Roman", 15), borderwidth=1, relief= "solid")
entry.grid(column=0, row=2, columnspan=4, padx=10, pady=10)

ido = Label(root, bg="#cce3de", text="Mostani eredmény: ")
ido.grid(column=0, row=3, columnspan=4, padx=10, pady=10)

best_ido = Label(root, bg="#cce3de", text="Legjobb eredmény: ")
best_ido.grid(column=0, row=4, columnspan=4, padx=10, pady=10)


start_gomb = Button(root, text="START", bg="#a4c3b2", font=("Arial", 12), command=randomszin).grid(row=5, column=1)























#futattás
root.mainloop()
