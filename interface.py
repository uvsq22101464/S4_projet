import tkinter as tk
from ethan import comptage_lettre

root = tk.Tk()
LONGUEUR, LARGEUR = 250, 250
#widgets
text = tk.StringVar()
boite_texte = tk.Entry(root, textvariable=text)
boite_texte.focus()
bouton_texte = tk.Button(root, text="récuper le texte", command=lambda : result.config(text=comptage_lettre(text.get())))
result = tk.Label(root, text="")

#placement des widgets
boite_texte.grid(row=1, column=0, columnspan=3, ipadx=100, ipady=10)
bouton_texte.grid(row=1, column=3)
result.grid()

root.mainloop()