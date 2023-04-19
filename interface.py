import tkinter as tk
from tkinter import filedialog
from langdetect import detect
from ethan import *
from fcts import *
import math


root = tk.Tk()
root.title("Projet crypto")
LONGUEUR, LARGEUR = 1500, 400


# fonctions :
def code_texte(dico: dict, text):
    """ 
    La focntion prend en argument un dicctionnaire et un text saisie par l'utilisateur.
    La focntion renvoie un text crypter selon le dictionnaire si la langue des deux textes
    est la même sinon elle renvoie un message 'ce n'est pas la meme langue'.
    """
    result = ""
    if verfi_lang() == True:
        for carac in text:
            try:
                result += dico[carac] + " "
            except:
                return f"le caractère {carac} n'est pas dans le texte servant a coder"
        return result
    else:
        return f"ce n'est pas la mmême langue"


def decrypte_texte(dico, text: str):
    """ 
    La focntion prend en argument un dicctionnaire et un text saisie par l'utilisateur.
    La focntion renvoie un text decrypter selon le dictionnaire.
    """
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
    # for carac in text:
    #    for key, val in dico.items():
    #        if val == carac:
    #            result += key
    return result


def getDictText(text):
    """
    La focntion prend en argument un text.
    Donne le dictionnaire du code associé au texte.
    """
    return ArbreB.codage(ArbreB.create_tree(Sommet.make_list(comptage_lettre(text))))


def dessin(canvas: tk.Canvas, arbre: ArbreB):
    """
    Ethan tu expliqueras :)
    """
    profondeur = ArbreB.profondeur_arbre(ArbreB.create_tree(
        Sommet.make_list(comptage_lettre(text.get())))) + 1
    largeur = ArbreB.largeur_arbre(arbre)
    posXSuivant = largeur[0] ** math.log2(profondeur)*1000
    # le * repésente l'écart qu'on veut donner/ encore a déterminer
    try:  # quand il y a un seul carac on a math domain error / peut être aussi pour d'autre taille de texte j'ai pas tout regarder
        taille = (largeur[1] * posXSuivant / 2**(math.log2(largeur[1])-1),
                  largeur[2] * posXSuivant / 2**(math.log2(largeur[2])-1))
    except:
        pass
    ArbreB.dessinerArbre(arbre, canvas, LARGEUR, largeur=largeur,
                         profondeur=profondeur, taille=taille, posXSuivant=posXSuivant)


def effacer_canvas(canvas: tk.Canvas):
    """
    La fonction prend en argument un canvas.
    Elle permet d'effacer les éléments dans le canvas
    """
    canvas.delete("all")


def language(langue):  # a changer
    """
    La fonction prend en argument la langue
    Elle permet de changer la langue selon la langue choisie par l'utilisateur.
    """
    if langue == "Francais":
        titre1.config(text="Entrez un texte pour obtenir un codage")
        bouton_texte.config(text="Générer le code")
        bouton_decrypte.config(text="décrypter")
        bouton_decode.config(text="crypter")
        bouton_open_file_a_crypter.config(text="ouvrir un fichier à crypter")
        bouton_open_file_a_decrypter.config(text="ouvrir fichier à decrypter")
        bouton_save_decrypter.config("sauvegarder le decryptage")
        bouton_save_crypter.config(text="sauvegarder le cryptage")
        bouton_save_cle.config(text="save encryption key")
        bouton_open_file_obtenir_code.config(
            text="ouvrir un fichier pour obtenir un codage")

    elif langue == "English":
        titre1.config(text="Enter text to get coding")
        bouton_texte.config(text="Generate the code")
        bouton_decrypte.config(text="Unencrypte")
        bouton_decode.config(text="encrypt")
        bouton_open_file_a_crypter.config(text="open a file to encrypt")
        bouton_open_file_a_decrypter.config(text="open file to decrypt")
        bouton_save_crypter.config(text="save encryption")
        bouton_save_decrypter.config(text="save decryption")
        bouton_save_cle.config(text="save key of encrypt")
        bouton_open_file_obtenir_code.config(text="open file to get coding")

    elif langue == "Español":
        titre1.config(text="Ingrese el texto para obtener la codificación")
        bouton_texte.config(text="Generar el código")
        bouton_decrypte.config(text="descifrar")
        bouton_decode.config(text="encriptar")
        bouton_open_file_a_crypter.config(text="abrir un archivo para cifrar")
        bouton_open_file_a_decrypter.config(
            text="abrir archivo para descifrar")
        bouton_save_crypter.config(text="guardar cifrado")
        bouton_save_decrypter.config("guardar descifrado")
        bouton_save_cle.config(text="guardar clave de cifrado")
        bouton_open_file_obtenir_code.config(
            text="abrir archivo para obtener codificación")


def afficher_dico():
    """
    La fonction ne prend pas d'argument.
    Elle permet d'afficher le dictionnaire contenant le codage dans la fenetre graphique.
    """
    if crypter["text"] == "":
        crypter.config(text=res_code + str(getDictText(text.get())))
        bouton_afficher.config(text=desaf_code)
    else:
        crypter.config(text="")
        bouton_afficher.config(text=af_code)


def test():
    """
    La focntion de prend pas d'argument.
    Elle permet de récuperer le texte des widgest dans la fenetre mais pas tout de toute façon c'est inutile.
    """
    liste_texte_widget = [af_code, desaf_code, res_code]
    for i in root.winfo_children():
        if type(i) != tk.Entry:
            try:
                liste_texte_widget.append(i['text'])
            except:
                pass
    print(liste_texte_widget)


def verfi_lang():
    """
    La fonction ne prend pas d'argument.
    Elle permet de connaitre la langue du texte ou les statitiques sont faites et la langue du texte à crypter.
    ELle renvoie Vrai si la langue est la meme sinon elle renvoie Faux.
    """
    langue_codage = detect(boite_texte.get())
    langue_text_a_crypter = detect(decode_label.get())
    if langue_codage == langue_text_a_crypter:
        return True
    else:
        return False


def open_file():
    """
    La fonction ne prend pas d'argument.
    Elle permet d'ouvir un fichier pour obtenir un texte.
    """
    file = filedialog.askopenfile()
    if file is not None:
        content = file.read()
        file.close()
        return content


def create_file():
    """
    La fonction ne prend pas d'argument.
    Elle permet de créer un fichier.
    """
    file = filedialog.askopenfile()
    if file is not None:
        content = file.read()
        print(content)
        file.close()


def save_text(text):
    """
    La fonction ne prend pas d'argument.
    Elle permet de sauvegarder le cryptage/decryptage d'un texte.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, "w") as f:
        f.write(text)


# widgets
text = tk.StringVar()
decrypte = tk.StringVar()
text_a_decoder = tk.StringVar()

option = tk.Menubutton(root, text="Choix Langues", relief="raised")
option.menu = tk.Menu(option)
liste_option = ["Francais", "English", "Español"]
for options in liste_option:
    option.menu.add_command(
        label=options, command=lambda options=options: language(options))
option["menu"] = option.menu
option.grid(row=0, column=0, sticky="w")


af_code, desaf_code, res_code = "afficher le codage", "désafficher le codage", "Résultat du codage : "
titre1 = tk.Label(root, text="Entrez un texte pour obtenir un codage")
titre1.grid(row=1, column=0)
bouton_open_file_obtenir_code = tk.Button(root, text="ouvrir un fichier pour avoir un code", command=lambda: [effacer_canvas(canvas), dessin(
    canvas, ArbreB.create_tree(Sommet.make_list(comptage_lettre(open_file())))), bouton_afficher.config(state="normal")], width=30)
bouton_open_file_obtenir_code.grid(row=1, column=1)
boite_texte = tk.Entry(root, textvariable=text, width=50)
boite_texte.grid(row=2, column=0)
boite_texte.focus()
bouton_texte = tk.Button(root, text="Générer le code", command=lambda: [effacer_canvas(canvas), dessin(
    canvas, ArbreB.create_tree(Sommet.make_list(comptage_lettre(text.get())))), bouton_afficher.config(state="normal")], width=30)
bouton_texte.grid(row=2, column=1)
bouton_afficher = tk.Button(
    root, text=af_code, command=afficher_dico, width=30, state="disabled")
bouton_afficher.grid(row=3, column=1)
crypter = tk.Label(root, text="", wraplength=300, anchor="e")
crypter.grid(row=3, column=0, columnspan=3)

titre3 = tk.Label(root, text="CRYPTAGE :")
titre3.grid(row=4, column=0, sticky="w")
bouton_open_file_a_crypter = tk.Button(root, text="ouvrir un fichier à crypter", command=lambda: result_codage.config(
    text=code_texte(getDictText(text.get()), open_file())), width=30)
bouton_open_file_a_crypter.grid(row=5, column=0)
decode_label = tk.Entry(root, textvariable=text_a_decoder)
decode_label.grid(row=6, column=0, ipadx=100, ipady=10)
bouton_decode = tk.Button(root, text="crypter", command=lambda: result_codage.config(
    text=code_texte(getDictText(text.get()), text_a_decoder.get())), width=30)
bouton_decode.grid(row=6, column=1)
result_codage = tk.Label(root, text="")
result_codage.grid(row=7, column=0)


titre2 = tk.Label(root, text="DECRYPTAGE :")
titre2.grid(row=8, column=0, sticky="w")
bouton_open_file_a_decrypter = tk.Button(root, text="ouvrir un fichier à decrypter", command=lambda: decrypter.config(
    text=decrypte_texte(getDictText(text.get()), open_file()), width=30))
bouton_open_file_a_decrypter.grid(row=8, column=0)
decrypte_label = tk.Entry(root, textvariable=decrypte)
decrypte_label.grid(row=9, column=0, ipadx=100, ipady=10)
# bouton_decrypte = tk.Buttol(root), text="Décrypter", command=lambda : decrypter.config(text=decrypte_texte(getDictText(text.get()),decrypte.get())), width=30)
bouton_decrypte = tk.Button(root, text="Décrypter", command=lambda: decrypter.config(
    text=decrypte_texte(getDictText(text.get()), decrypte.get())), width=30)
bouton_decrypte.grid(row=9, column=1)
decrypter = tk.Label(root, text="")
decrypter.grid(row=10, column=0)


frame = tk.Frame(root, height=LARGEUR, width=LONGUEUR)
canvas = tk.Canvas(frame, height=LARGEUR, width=LONGUEUR,
                   bg="white", scrollregion=(-200, -10, 1000, 1000))
xbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
ybar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
xbar.pack(side="bottom", fill="x")
ybar.pack(side="right", fill="y")
canvas.config(xscrollcommand=xbar.set, yscrollcommand=ybar.set)
canvas.pack(expand=True, fill="both")
frame.grid(row=11, columnspan=2, column=0)


# bouton open file
bouton_save_cle = tk.Button(root, text="sauvegarder la clé de cryptage",
                            command=lambda: save_text(crypter.cget("text")))
bouton_save_cle.grid(row=3, column=0, sticky="w")
bouton_save_crypter = tk.Button(
    root, text="sauvegarder le cryptage", command=lambda: save_text(result_codage.cget("text")))
bouton_save_crypter.grid(row=7, column=0, sticky="w")
bouton_save_decrypter = tk.Button(
    root, text="sauvegarder le decryptage", command=lambda: save_text(decrypter.cget("text")))
bouton_save_decrypter.grid(row=1, column=5, sticky="w")


root.mainloop()



# TACHES A TERMINER 90%:


#  améliorer module arbre
#  vérifier les bugs
#  contre-rendue
#  améliorer l'interface
#  recréer les apps windows/mac

