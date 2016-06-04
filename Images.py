from PIL import Image, ImageTk ## Importation des modules utiles dans PIL
import  tkinter as Tk

def suivant():
	if nomimage["text"]=="Exemplepourlecodinggoûter.jpg":
		nomimage["text"] = "img2.jpg"
	else:
		nomimage["text"] = "Exemplepourlecodinggoûter.jpg"
	monimage = Image.open(nomimage["text"])
	photo = ImageTk.PhotoImage(monimage)
	label["image"] = photo    ## Insertion de l'image
	label.image = photo 			## Maintient en vie de photo dans un objet non détruit par le garbage

root = Tk.Tk()
monimage = Image.open("Exemplepourlecodinggoûter.jpg")    ## Chargement d'une image à partir de PIL
photo = ImageTk.PhotoImage(monimage)   ## Création d'une image compatible Tkinter

label = Tk.Label(image=photo)    ## Insertion de l'image
label.image = photo 			## Maintient en vie de photo dans un objet non détruit par le garbage
								## pour pas que l'image disparaisse du label
label.pack()

nomimage = Tk.Label(text="Exemplepourlecodinggoûter.jpg")

# Il faut ajouter les boutons :
bouton_quitter = Tk.Button(root, text="✖ Quitter", fg="red", command=root.quit)
bouton_quitter.pack(side="left")
bouton_cliquer = Tk.Button(root, text="Suivant →", fg="green",command=suivant)
bouton_cliquer.pack(side="right")

root.mainloop()
