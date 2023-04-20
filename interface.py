import tkinter as tk
from tkinter import filedialog
from langdetect import detect_langs
from module_arbre import *
import math

root = tk.Tk()
root.title("Projet crypto")
LONGUEUR, LARGEUR = 1200, 400

# fonctions :
def comptage_lettre(text):
    """
    Prends une chaîne de caractères en entrée et renvoi
    une liste de tuple contenant les lettres qui apparaissent
    dans le texte et leur nombre d'occurrences.
    """
    liste = []
    for elem in set(text):
        liste.append((elem, text.count(elem)))
    return sorted(liste, key=lambda x : x[1])


def getDictText(arbre):
    """
    Prends en entrée un ArbreB
    Donne le dictionnaire associé à l'arbre.
    """
    return ArbreB.codage(arbre)


def code_texte(dico, text):
    """ 
    La fonction prend en argument un dictionnaire et un texte saisi par l'utilisateur.
    La fonction renvoie un texte crypté selon le dictionnaire si la langue des deux textes
    est la même sinon elle renvoie un message "ce n'est pas la même langue".
    """
    result = ""
    if verfi_lang() == True:
        for carac in text:
            try:
                result += dico[carac] + " "
            except:
                return f"{carac} {erreur_carac}"
        return result
    else:
        return f"{pas_meme_langue}"


def decrypte_texte(dico, text: str):
    """ 
    La fonction prend en argument un dictionnaire et un texte saisi par l'utilisateur.
    La fonction renvoie un texte décrypter selon le dictionnaire.
    """
    result = ""
    tmp = ""
    for i in range(len(text)):
        if text[i] == " ":
            continue
        tmp += text[i]
        for key, val in dico.items():
            if val == tmp:
                result += key
                tmp = ""
    if detection_langue(detect_langs(result)) == detection_langue(detect_langs(texte_codant)):
        return result
    else:
        return f"{result} | {pas_bonne_cle}"


def dessin(canvas: tk.Canvas, arbre: ArbreB):
    """
    Prends en argument un canvas et un ArbreB
    La fonction permet de dessiner l'arbre sur le canvas.
    """
    profondeur = ArbreB.profondeur_arbre(arbre) + 1
    largeur = ArbreB.largeur_arbre(arbre)    
    nb_noeud = (arbre.nb_noeud()-1)
    coef = nb_noeud + (largeur[0] * profondeur / nb_noeud) if largeur[0] ** math.log2(profondeur) <= 90 else nb_noeud*1.5 / (largeur[0] * profondeur)
    posXSuivant = (largeur[0] ** math.log2(profondeur)) * coef
    try:
        taille = (largeur[1] * posXSuivant / 2**(math.log2(largeur[1])-1),
                  largeur[2] * posXSuivant / 2**(math.log2(largeur[2])-1))
    except:
        pass
    ArbreB.dessinerArbre(arbre, canvas, LARGEUR, largeur=largeur,
                         profondeur=profondeur, taille=taille, posXSuivant=posXSuivant)


def effacer_canvas(canvas: tk.Canvas):
    """
    La fonction prend en argument un canvas.
    Elle permet d'effacer les éléments dans le canvas.
    """
    canvas.delete("all")


def language(langue):
    """
    La fonction prend en argument la langue
    Elle permet de changer la langue de la fenêtre selon la langue choisie par l'utilisateur.
    """
    global erreur_carac, desaf_code, af_code, pas_meme_langue, pas_bonne_cle
    if langue == "Francais" or langue == "fr":
        titre1.config(text="Entrer un texte pour obtenir un code")
        titre2.config(text ="Décryptage : entrer un texte à décrypter")
        titre3.config(text ="Cryptage : entrer un texte à crypter")
        bouton_texte.config(text="Générer le code")
        bouton_decrypte.config(text="Décrypter")
        bouton_decode.config(text="Crypter")
        bouton_open_file_a_crypter.config(text="Ouvrir un fichier à crypter")
        bouton_open_file_a_decrypter.config(text="Ouvrir un fichier à décrypter")
        bouton_save_crypter.config(text="Sauvegarder le cryptage")
        bouton_save_decrypter.config(text="Sauvegarder le décryptage")
        bouton_save_cle.config(text="Sauvegarder la clé de cryptage")
        bouton_open_file_obtenir_code.config(text="Ouvrir un fichier pour avoir un code")
        option.config(text="Choix Langue")
        erreur_carac = "n'est pas dans le texte servant à coder"
        bouton_afficher.config(text="Afficher le code" if bouton_afficher["text"] == af_code else "Désafficher le code")
        desaf_code = "Désafficher le code"
        af_code = "Afficher le code"
        pas_meme_langue = "Ce n'est pas la même langue"
        pas_bonne_cle = "Ce n'est pas la bonne clé"

    elif langue == "English" or langue == "en":
        titre1.config(text="Enter text to get coding")
        titre2.config(text ="Decryption : ")
        titre3.config(text ="Encryption : ")
        bouton_texte.config(text="Generate the code")
        bouton_decrypte.config(text="Unencrypt")
        bouton_decode.config(text="Encrypt")
        bouton_open_file_a_crypter.config(text="Open a file to encrypt")
        bouton_open_file_a_decrypter.config(text="Open a file to decrypt")
        bouton_save_crypter.config(text="Save encryption")
        bouton_save_decrypter.config(text="Save decryption")
        bouton_save_cle.config(text="Save key of encrypt")
        bouton_open_file_obtenir_code.config(text="Open file to get coding")
        option.config(text="Choose language")
        erreur_carac = "isn't in the coding text"
        bouton_afficher.config(text="Show the code" if bouton_afficher["text"] == af_code else "Hide the code")
        desaf_code = "Hide the code"
        af_code = "Show the code"
        pas_meme_langue = "This is not the same language"
        pas_bonne_cle = "This is not the right key"

    elif langue == "Español" or langue == "es":
        titre1.config(text="Ingrese el texto para obtener la codificación")
        titre2.config(text ="Cifrado : ")
        titre3.config(text ="Descifrado : ")
        bouton_texte.config(text="Generar el código")
        bouton_decrypte.config(text="Descifrar")
        bouton_decode.config(text="Encriptar")
        bouton_open_file_a_crypter.config(text="Abrir un archivo para cifrar")
        bouton_open_file_a_decrypter.config(text="Abrir archivo para descifrar")
        bouton_save_crypter.config(text="Guardar cifrado")
        bouton_save_decrypter.config(text="Guardar descifrado")
        bouton_save_cle.config(text="Guardar clave de cifrado")
        bouton_open_file_obtenir_code.config(text="Abrir archivo para obtener codificación")
        option.config(text="Elección de la lengua")
        erreur_carac = "no figura en el texto utilizado para codificar"
        bouton_afficher.config(text="Visualizar el código" if bouton_afficher["text"] == af_code else "Desactivar el código")
        desaf_code = "Desactivar el código"
        af_code = "Visualizar el código"
        pas_meme_langue = "No es la misma lengua"
        pas_bonne_cle = "Esta no es la llave correcta"

    elif langue == "Deutsch" or langue == "de":
        titre1.config(text="Öffnen Sie die Datei, um die Codierung zu erhalten")
        titre2.config(text ="Entschlüsselung : ")
        titre3.config(text ="Verschlüsselung : ")
        bouton_texte.config(text="Generieren Sie den Code")
        bouton_decrypte.config(text="Entschlüsseln")
        bouton_decode.config(text="Verschlüsseln")
        bouton_open_file_a_crypter.config(text="Öffnen Sie eine zu verschlüsselnde Datei")
        bouton_open_file_a_decrypter.config(text="Datei zum Entschlüsseln öffnen")
        bouton_save_crypter.config(text="Verschlüsselung speichern")
        bouton_save_decrypter.config(text="Entschlüsselung speichern")
        bouton_save_cle.config(text="Schlüssel zum Verschlüsseln speichern")
        bouton_open_file_obtenir_code.config(text="Öffnen Sie die Datei, um die Codierung zu erhalten")
        option.config(text="Wahl der Sprache")
        erreur_carac = "ist nicht in dem Text enthalten, der zum Verschlüsseln dient"
        bouton_afficher.config(text="Code anzeigen" if bouton_afficher["text"] == af_code else "Code ausblenden")
        desaf_code = "Code ausblenden"
        af_code = "Code anzeigen"
        pas_meme_langue = "Es ist nicht dieselbe Sprache"
        pas_bonne_cle = "Es ist nicht der richtige Schlüssel"

    elif langue == "中国人" or langue == "zh-cn":
        titre1.config(text="输入文字获取编码")
        titre2.config(text ="解密 : ")
        titre3.config(text ="加密 : ")
        bouton_texte.config(text="生成代码")
        bouton_decrypte.config(text="解密")
        bouton_decode.config(text="加密")
        bouton_open_file_a_crypter.config(text="打开要加密的文件")
        bouton_open_file_a_decrypter.config(text="打开文件解密")
        bouton_save_crypter.config(text="保存加密")
        bouton_save_decrypter.config(text="保存解密")
        bouton_save_cle.config(text="保存加密密钥")
        bouton_open_file_obtenir_code.config(text="打开文件进行编码")
        option.config(text="语言的选择")
        erreur_carac = "不在用于编码的文本中"
        bouton_afficher.config(text="显示代码" if bouton_afficher["text"] == af_code else "禁用代码")
        desaf_code = "禁用代码"
        af_code = "显示代码"
        pas_meme_langue = "不是同一种语言"
        pas_bonne_cle = "这不是正确的钥匙"


def detection_langue(l_proba, liste_langue=["fr", "en", "es", "de", "zh-cn"]):
    """
    Prends en argument le résultat de la fonction detect_langs qui est une liste de probabilité
    et retourne celle qui est la plus probable parmi les langues dans la liste_langue ou français si la langue n'est pas dans la liste.
    """
    for i in range(len(l_proba)):
        langue = str(l_proba[i])[:2]
        if langue in liste_langue:
            return langue
        else:
            continue
    return "fr"


def afficher_dico():
    """
    La fonction ne prend pas d'argument.
    Elle permet d'afficher le dictionnaire contenant le codage dans la fenêtre graphique.
    """
    if crypter["text"] == "":
        crypter.config(text=str(dict))
        bouton_afficher.config(text=desaf_code)
    else:
        crypter.config(text="")
        bouton_afficher.config(text=af_code)


def verfi_lang():
    """
    La fonction ne prend pas d'argument.
    Elle permet de connaitre la langue du texte où les statistiques sont faites et la langue du texte à crypter.
    Elle renvoie Vrai si la langue est la même sinon elle renvoie Faux.
    """
    langue_codage = detection_langue(detect_langs(texte_codant))
    langue_text_a_crypter = detection_langue(detect_langs(texte_a_crypter))
    if langue_codage == langue_text_a_crypter:
        return True
    else:
        return False


def open_file(parametre):
    """
    La fonction ne prend pas d'argument.
    Elle permet d'ouvrir un fichier pour obtenir un texte.
    """
    global texte_codant, texte_a_crypter, texte_a_decrypter
    file = filedialog.askopenfile()
    if file is not None and parametre == 0:
        texte_codant = file.read()
        file.close()
        return texte_codant
    if file is not None and parametre == 1:
        texte_a_crypter = file.read()
        file.close()
        return texte_a_crypter
    if file is not None and parametre == 2:
        texte_a_decrypter = file.read()
        file.close()
        return texte_a_decrypter


def save_text(text):
    """
    La fonction prend en argument un texte.
    Elle permet de sauvegarder le cryptage/décryptage d'un texte.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, "w") as f:
        f.write(text)


def nouv_arbre(text):
    """
    La fonction prend un texte en argument et permet d'instancier un arbre, son texte et son dictionnaire.
    """
    global arbre, texte_codant, dict
    arbre = ArbreB.create_tree(Sommet.make_list(comptage_lettre(text)))
    texte_codant = text
    dict = ArbreB.codage(arbre)
    language(detection_langue(detect_langs(texte_codant)))
    return arbre, texte_codant, dict


def getTextDecrypter(text):
    """
    La fonction permet de récupérer le texte à décrypter.
    """
    global texte_a_crypter
    texte_a_crypter = text
    return texte_a_crypter


# Initialisation des variables
arbre = None
texte_codant = None
dict = None
texte_a_crypter = None
texte_a_decrypter = None
text = tk.StringVar()
decrypte = tk.StringVar()
text_a_decoder = tk.StringVar()
af_code, desaf_code = "Afficher le code", "Désafficher le code"
erreur_carac = "n'est pas dans le texte servant à coder"
pas_meme_langue = "Ce n'est pas la même langue"
pas_bonne_cle = "Ce n'est pas la bonne clé"

# Bouton changer de langue
option = tk.Menubutton(root, text="Choix Langues", relief="raised")
option.menu = tk.Menu(option)
liste_option = ["Francais", "English", "Español","Deutsch","中国人"]
for options in liste_option:
    option.menu.add_command(
        label=options, command=lambda options=options: language(options))
option["menu"] = option.menu
option.grid(row=0, column=0, sticky="w")

# bouton open file
bouton_save_cle = tk.Button(root, text="Sauvegarder la clé de cryptage",
                            command=lambda: save_text(str(getDictText(text.get()))), state="disabled")
bouton_save_cle.grid(row=3, column=0, sticky="w")

bouton_save_crypter = tk.Button(root, text="Sauvegarder le cryptage",
                                command=lambda: save_text(result_codage.cget("text")), state="disabled")
bouton_save_crypter.grid(row=7, column=0, sticky="w")

bouton_save_decrypter = tk.Button(root, text="Sauvegarder le decryptage",
                                  command=lambda: save_text(decrypter.cget("text")), state="disabled")
bouton_save_decrypter.grid(row=1, column=5, sticky="w")


titre1 = tk.Label(root, text="Entrer un texte pour obtenir un code")
titre1.grid(row=1, column=0)

bouton_open_file_obtenir_code = tk.Button(root, text="Ouvrir un fichier pour avoir un code", command=lambda: [effacer_canvas(canvas), nouv_arbre(open_file(0)),
                                          dessin(canvas, arbre), bouton_afficher.config(state="normal"), bouton_save_cle.config(state="normal"),
                                          bouton_decode.config(state="normal"), bouton_decrypte.config(state="normal")], width=30)
bouton_open_file_obtenir_code.grid(row=1, column=1)

boite_texte = tk.Entry(root, textvariable=text)
boite_texte.grid(row=2, column=0, ipadx=100, ipady=10)
boite_texte.focus()

bouton_texte = tk.Button(root, text="Générer le code", command=lambda: [effacer_canvas(canvas), nouv_arbre(text.get()),
                         dessin(canvas, arbre), bouton_afficher.config(state="normal"), bouton_save_cle.config(state="normal"),
                         bouton_decode.config(state="normal"), bouton_decrypte.config(state="normal")], width=30)
bouton_texte.grid(row=2, column=1)

bouton_afficher = tk.Button(root, text=af_code, command=afficher_dico, width=30, state="disabled")
bouton_afficher.grid(row=3, column=1)

crypter = tk.Label(root, text="", wraplength=300, anchor="e")
crypter.grid(row=3, column=0, columnspan=3)

titre3 = tk.Label(root, text="Cryptage : entrer un texte à crypter")
titre3.grid(row=4, column=0, sticky="w")

bouton_open_file_a_crypter = tk.Button(root, text="Ouvrir un fichier à crypter", command=lambda: (result_codage.config(text=
                                       code_texte(getDictText(arbre), open_file(1))), bouton_save_crypter.config(state="normal")), width=30)
bouton_open_file_a_crypter.grid(row=5, column=0)

decode_label = tk.Entry(root, textvariable=text_a_decoder)
decode_label.grid(row=6, column=0, ipadx=100, ipady=10)

bouton_decode = tk.Button(root, text="Crypter", command=lambda: (result_codage.config(text=
                          code_texte(getDictText(arbre), getTextDecrypter(text_a_decoder.get()))), bouton_save_crypter.config(state="normal")),
                          width=30, state="disabled")
bouton_decode.grid(row=6, column=1)

result_codage = tk.Label(root, text="")
result_codage.grid(row=7, column=0)

titre2 = tk.Label(root, text="Décryptage : entrer un texte à décrypter")
titre2.grid(row=8, column=0, sticky="w")

bouton_open_file_a_decrypter = tk.Button(root, text="Ouvrir un fichier à décrypter", command=lambda: (decrypter.config(text=
                                         decrypte_texte(dict, open_file(2))), bouton_save_decrypter.config(state="normal")), width=30)
bouton_open_file_a_decrypter.grid(row=8, column=0)

decrypte_label = tk.Entry(root, textvariable=decrypte)
decrypte_label.grid(row=9, column=0, ipadx=100, ipady=10)

bouton_decrypte = tk.Button(root, text="Décrypter", command=lambda: (decrypter.config(text=
                            decrypte_texte(dict, decrypte.get())), bouton_save_decrypter.config(state="normal")), width=30, state="disabled")
bouton_decrypte.grid(row=9, column=1)

decrypter = tk.Label(root, text="")
decrypter.grid(row=10, column=0)

# Canvas et scrollbars
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

root.mainloop()
