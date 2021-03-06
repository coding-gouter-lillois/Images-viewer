#!/usr/bin/python
from PIL import Image, ImageTk ## Importation des modules utiles dans PIL
try:
    import Tkinter as Tk
except ImportError:
    import tkinter as Tk

def suivant():
	if nomimage["text"]=="Example.jpg":
		nomimage["text"] = "Doudou.jpg"
	else:
		nomimage["text"] = "Example.jpg"
	mon_image = Image.open(nomimage["text"])
	photo = ImageTk.PhotoImage(mon_image)
	label["image"] = photo
	label.image = photo

root = Tk.Tk()
mon_image = Image.open("Example.jpg")
photo = ImageTk.PhotoImage(mon_image)

label = Tk.Label(image=photo)
label.image = photo

label.pack()

nomimage = Tk.Label(text="Example.jpg")

# Ajouter les boutons :
bouton_cliquer = Tk.Button(root, text="Suivant ->", fg="green", command=suivant)
bouton_cliquer.pack(side="right")
bouton_quitter = Tk.Button(root, text="X Quitter", fg="red", command=root.quit)
bouton_quitter.pack(side="right")

root.mainloop()
