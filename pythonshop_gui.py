from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import simpledialog


def zapisz():
    global obraz
    save_path = filedialog.asksaveasfilename(initialdir = "/", title = "Select file", filetypes = (("JPG","*.jpg"),("Wszystkie pliki","*.*")))
    save_path+=".jpg"
    obraz.save(save_path)

def obrot():
    global obraz
    stopnie=simpledialog.askinteger("Obracanie", "Wprowadź liczbę stopni", parent=root)
    obraz = obraz.rotate(stopnie)
    photo_space.image=ImageTk.PhotoImage(obraz)
    photo_space.configure(image=photo_space.image)  

def skaluj():
    global obraz
    y=simpledialog.askinteger("Skalowanie", "Wprowadź wysokość", parent=root)
    x=simpledialog.askinteger("Skalowanie", "Wprowadź szerokość", parent=root)
    obraz = obraz.resize((x,y))
    photo_space.image=ImageTk.PhotoImage(obraz)
    photo_space.configure(image=photo_space.image)

root=Tk()
root.title("Pythonshop")
root.geometry("1200x600")
root.resizable(False, False)

menu_bar=Menu(root)
menu_file=Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Plik", menu=menu_file)
menu_file.add_command(label="Zapisz jako", command=zapisz)
menu_file.add_separator()
menu_file.add_command(label="Wyjdź", command=root.quit)

photo_space=Label(root, width=1100, height=600)
photo_space.grid(column=0, rowspan=6)

sidebar=Frame(root, width=100).grid(column=1)
obroc_sidebar=Button(sidebar, text="Obróć", command=obrot).grid(row=0, column=1, sticky="nesw")
skaluj_sidebar=Button(sidebar, text="Skaluj", command=skaluj).grid(row=1, column=1, sticky="nesw")
czarno_bialy_sidebar=Button(sidebar, text="Czarno-biały").grid(row=2, column=1, sticky="nesw")
spacer_sidebar=Frame(sidebar, height=300).grid(row=3, column=1, sticky="nesw")

obraz_path=filedialog.askopenfilename(initialdir = "/", title = "Wybierz plik", filetypes = (("JPG","*.jpg"),("Wszystkie pliki","*.*")))
obraz=Image.open(obraz_path)
obrazTK=ImageTk.PhotoImage(obraz)
photo_space.configure(image=obrazTK)
photo_space.image = obrazTK

root.config(menu=menu_bar)
root.mainloop()
