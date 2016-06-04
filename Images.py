from PIL import Image, ImageTk ## Importation des modules utiles dans PIL
import  tkinter as Tk

def suivant():
	if nomimage["text"]=="Example.jpg":
		nomimage["text"] = "Doudou.jpg"
	else:
		nomimage["text"] = "Example.jpg"
	monimage = Image.open(nomimage["text"])
	photo = ImageTk.PhotoImage(monimage)
	label["image"] = photo
	label.image = photo

root = Tk.Tk()
monimage = Image.open("Example.jpg")
photo = ImageTk.PhotoImage(monimage)

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
