import tkinter as tk
from ethan import comptage_lettre, ArbreB, Sommet
import math
# importer langdetect ou textblob (moins bien)
root = tk.Tk()
LONGUEUR, LARGEUR = 600, 400

def code_texte(dico : dict, text):
    result = ""
    for carac in text:
        try:
            result += dico[carac] + " "
        except:
            return f"le caractère {carac} n'est pas dans le texte servant a coder"
    return result

def decrypte_texte(dico, text : str):
    result = ""
    tmp = ""
    #text = text.split()
    for i in range(len(text)):
        if text[i] == " ":
            continue
        tmp += text[i]
        for key, val in dico.items():
            if val == tmp:
                result += key
                tmp = ""
    #for carac in text:
    #    for key, val in dico.items():
    #        if val == carac:
    #            result += key
    return result

def getDictText(text):
    """Donne le dictionnaire du code associé au texte"""
    return ArbreB.codage(ArbreB.create_tree(Sommet.make_list(comptage_lettre(text))))

def dessinerArbre(canvas : tk.Canvas, arbre, x=LONGUEUR//2, y=0, taille=1, cpt=1, maximum=(0, 0)):
    if type(arbre) == ArbreB:
        arbre = arbre.racine
    if arbre.fils_gauche == None and arbre.fils_droit == None:
        color = "royalblue" 
    else:
        color = "red"
        canvas.create_line(x, y, x-LONGUEUR//4//cpt, y+LARGEUR//(math.log2(taille)+2), arrow="last", fill="black", tags="left_arrow")
        canvas.create_line(x, y, x+LONGUEUR//4//cpt, y+LARGEUR//(math.log2(taille)+2), arrow="last", fill="black", tags="right_arrow")

    canvas.create_oval(x-200/taille, y, x+200/taille, y+200/taille*2, fill=color, tags=arbre.nom if len(arbre.nom) == 1 else ())
    canvas.create_text(x, y+15, text=arbre.nom, fill="black")

    if arbre.fils_gauche != None and arbre.fils_droit != None:
        return dessinerArbre(canvas, arbre.fils_gauche, x-LONGUEUR//4//cpt, y+LARGEUR//(math.log2(taille)+2), taille+1.5, cpt+1, maximum),\
               dessinerArbre(canvas, arbre.fils_droit, x+LONGUEUR//4//cpt, y+LARGEUR//(math.log2(taille)+2), taille+1.5, cpt+1, maximum)
    # ajuste la taille du canvas en fonction de si ça dépasse
    maximum = (max(maximum[0], x+LONGUEUR//4//cpt), min(maximum[1], x-LONGUEUR//4//cpt))
    canvas.config(width=maximum[0] + abs(maximum[1]))
    for items in canvas.find_all():
        if "right_arrow" in canvas.gettags(items):  # les flèches de droites ne se décallent pas bien :/
            canvas.move(items, abs(maximum[1])//taille+1.5, 0)
        else:
            canvas.move(items, abs(maximum[1])//taille+1.5, 0)
        pass
    # ajouter une sorte de tuto / aide pour découvrir l'app
    # changer le cpt car c'est en partie ce qui fait que ça se croise

def effacer_canvas(canvas : tk.Canvas):
    canvas.delete("all")

def language(langue):  # a changer
    if langue == "Francais":
        bouton_texte.config(text="récuperer texte")
        bouton_decrypte.config(text="décrypter")
    elif langue == "English":
        bouton_texte.config(text="Encrypte")
        bouton_decrypte.config(text="Unencrypte")
    else:
        bouton_texte.config(text="No hablo español")
        bouton_decrypte.config(text="como esta")

def afficher_dico():
    if crypter["text"] == "":
        crypter.config(text=res_code + str(getDictText(text.get())))
        bouton_afficher.config(text=desaf_code)
    else:
        crypter.config(text="")
        bouton_afficher.config(text=af_code)

def test():
    """récupe le texte des widgest dans la fenetre mais pas tout de toute façon c'est inutile"""
    liste_texte_widget = [af_code, desaf_code, res_code]
    for i in root.winfo_children():
            if type(i) != tk.Entry:
                try:
                    liste_texte_widget.append(i['text'])
                except:
                    pass
    print(liste_texte_widget)


#widgets
text = tk.StringVar()
decrypte = tk.StringVar()
text_a_decoder = tk.StringVar()

option = tk.Menubutton(root, text="Options", relief="raised")
option.menu = tk.Menu(option)
liste_option = ["Francais", "English", "Español"]
for options in liste_option:
    option.menu.add_command(label=options, command=lambda options=options: language(options))
option["menu"] = option.menu
option.grid(row=0, column=0, sticky="w")


frame_part1 = tk.Frame(root)
af_code, desaf_code, res_code = "afficher le codage", "désafficher le codage", "Résultat du codage : "
titre1 = tk.Label(frame_part1, text="Entrez un texte pour obtenir un codage")
titre1.grid(row=0, column=0, sticky="w")
boite_texte = tk.Entry(frame_part1, textvariable=text, width=50)
boite_texte.grid(row=1, column=0, sticky="w")
boite_texte.focus()
bouton_texte = tk.Button(frame_part1, text="Générer le code" , command=lambda : [effacer_canvas(canvas), dessinerArbre(canvas, ArbreB.create_tree(Sommet.make_list(comptage_lettre(text.get()))), taille=len(comptage_lettre(text.get()))), bouton_afficher.config(state="normal")], width=30)
bouton_texte.grid(row=1, column=2)
bouton_afficher = tk.Button(frame_part1, text=af_code, command=afficher_dico, width=30, state="disabled")
bouton_afficher.grid(row=2, column=2)
crypter = tk.Label(frame_part1, text="", wraplength=300, anchor="e")
crypter.grid(row=2, column=0, sticky="w", columnspan=3)
frame_part1.grid(row=1, column=0, columnspan=2)

frame_part2 = tk.Frame(root, bg="white")
titre2 = tk.Label(frame_part2, text="titre du frame 2")
titre2.grid(row=1, column=0, sticky="w")
decrypte_label = tk.Entry(frame_part2, textvariable=decrypte)
decrypte_label.grid(row=2, column=0, columnspan=3, ipadx=100, ipady=10)
bouton_decrypte = tk.Button(frame_part2, text="Décrypter", command=lambda : decrypter.config(text=decrypte_texte(getDictText(text.get()),decrypte.get())), width=30)
bouton_decrypte.grid(row=2, column=4)
decrypter = tk.Label(frame_part2, text="")
decrypter.grid(row=3, column=0, sticky="w")
frame_part2.grid(row=2, column=0)

frame_part3 = tk.Frame(root, bg="white")
titre3 = tk.Label(frame_part3, text="titre du frame 1")
titre3.grid(row=0, column=0, sticky="w")
decode_label = tk.Entry(frame_part3, textvariable=text_a_decoder)
decode_label.grid(row=1, column=0, columnspan=3, ipadx=100, ipady=10)
bouton_decode = tk.Button(frame_part3, text="décoder le texte", command=lambda : result_codage.config(text=code_texte(getDictText(text.get()), text_a_decoder.get())), width=30)
bouton_decode.grid(row=1, column=4)
result_codage = tk.Label(frame_part3, text="")
result_codage.grid(row=2, column=0, sticky="w")
frame_part3.grid(row=2, column=1)


frame = tk.Frame(root, height=LARGEUR, width=LONGUEUR)
canvas = tk.Canvas(frame, height=LARGEUR, width=LONGUEUR, bg="white", scrollregion=(-200, -10, 1000, 1000))
xbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
ybar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
xbar.pack(side="bottom", fill="x")
ybar.pack(side="right", fill="y")
canvas.config(xscrollcommand=xbar.set, yscrollcommand=ybar.set)
canvas.pack(expand=True, fill="both")
frame.grid(row=3, column=0, columnspan=2)

root.mainloop()
