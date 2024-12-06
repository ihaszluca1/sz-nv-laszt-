from tkinter import *
import random
import time

# Ablak létrehozása
root = Tk()
root.title("Színválasztó")
root.config(bg="#cce3de")

# Globális változók
colors = ["piros", "zöld", "kék", "sárga", "narancs", "lila", "barna", "fekete", "fehér"]
tk_colors = ["red", "green", "blue", "yellow", "orange", "magenta", "brown", "black", "white"]
current_color = ""
current_word = ""
start_time = 0
best_time = float('inf')

# Szín-generátor funkció
def random_color():
    global current_color, current_word, start_time
    num_colors = int(clicked.get())
    random_indices = random.sample(range(len(colors)), num_colors)
    word_index = random.choice(random_indices)
    color_index = random.choice(random_indices)
    
    current_word = colors[word_index]
    current_color = tk_colors[color_index]
    
    label_color.config(text=current_word, fg=current_color)
    feedback_label.config(text="")
    entry.delete(0, END)
    start_time = time.time()

# Ellenőrzés funkció
def check_answer():
    global best_time
    user_input = entry.get().strip().lower()
    elapsed_time = time.time() - start_time

    if user_input == current_color:
        feedback_label.config(text="Helyes!", fg="green")
        elapsed_time_label.config(text=f"Eltelt idő: {elapsed_time:.2f} mp")
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_time_label.config(text=f"Legjobb idő: {best_time:.2f} mp")
        # Automatikusan új szót generál
        random_color()
    else:
        feedback_label.config(text=f"Helytelen! A helyes válasz: {current_color}", fg="red")
    entry.delete(0, END)

# Dropdown menü a színek számának beállítására
szamok = [str(i) for i in range(2, 9)]
clicked = StringVar()
clicked.set("2")

dropdown_label = Label(root, text="Hány szín legyen?", bg="#cce3de", font=("Arial", 12))
dropdown_label.grid(column=0, row=0, padx=5, pady=5)

dropdown = OptionMenu(root, clicked, *szamok)
dropdown.grid(column=1, row=0, padx=5, pady=5)

# Szó kiírása színnel
label_color = Label(root, text="", font=("Arial", 20), bg="#cce3de")
label_color.grid(column=0, row=1, columnspan=2, pady=10)

# Felhasználói beviteli mező
entry = Entry(root, width=20, font=("Arial", 15), borderwidth=2, relief="solid", justify="center")
entry.grid(column=0, row=2, columnspan=2, padx=5, pady=10)

# Eredmény kijelzése
elapsed_time_label = Label(root, text="Eltelt idő: ", bg="#cce3de", font=("Arial", 12))
elapsed_time_label.grid(column=0, row=3, columnspan=2, pady=5)

best_time_label = Label(root, text="Legjobb idő: ", bg="#cce3de", font=("Arial", 12))
best_time_label.grid(column=0, row=4, columnspan=2, pady=5)

feedback_label = Label(root, text="", bg="#cce3de", font=("Arial", 12))
feedback_label.grid(column=0, row=5, columnspan=2, pady=5)

# Gombok
start_button = Button(root, text="START", command=random_color, bg="#a4c3b2", font=("Arial", 12))
start_button.grid(column=0, row=6, padx=5, pady=10)

check_button = Button(root, text="ELLENŐRZÉS", command=check_answer, bg="#a4c3b2", font=("Arial", 12))
check_button.grid(column=1, row=6, padx=5, pady=10)

# Futtatás
root.mainloop()
