import tkinter as tk
from ethan import comptage_lettre, ArbreB, Sommet

root = tk.Tk()
LONGUEUR, LARGEUR = 300, 300

def code_text(dico : dict, text):
    result = ""
    for carac in text:
        result += dico[carac] + " "
    return result

def decrypte_texte(dico, text : str):
    result = ""
    text = text.split()
    for carac in text:
        for key, val in dico.items():
            if val == carac:
                result += key
    return result

#widgets
text = tk.StringVar()
decrypte = tk.StringVar()
boite_texte = tk.Entry(root, textvariable=text)
boite_texte.focus()
bouton_texte = tk.Button(root, text="récuper le texte", command=lambda : result.config(text=code_text(ArbreB.codage_arbre(ArbreB.create_tree(Sommet.make_list(comptage_lettre(text.get())))),text.get())))
result = tk.Label(root, text="")
decrypte_label = tk.Entry(root, textvariable=decrypte)
bouton_decrypte = tk.Button(root, text="Décrypter", command=lambda : result.config(text=decrypte_texte(ArbreB.codage_arbre(ArbreB.create_tree(Sommet.make_list(comptage_lettre(text.get())))),decrypte.get())))
canvas = tk.Canvas(root, height=LONGUEUR, width=LARGEUR, bg="white")



#placement des widgets
boite_texte.grid(row=1, column=0, columnspan=3, ipadx=100, ipady=10)
bouton_texte.grid(row=1, column=3)
result.grid()
decrypte_label.grid()
bouton_decrypte.grid()
canvas.grid()


def draw_tree(canvas):
    canvas.create_oval(LONGUEUR//2, 5, LONGUEUR//2+5, 10, outline="black", fill="black")

draw_tree(canvas)

root.mainloop()