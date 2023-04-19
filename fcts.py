from ethan import *



def comptage_lettre(text):
    """prend une chaîne de caractère en entrée et renvoi
    une liste de tuplecontenant les lettres qui apparaissent
    dans le text et leur nombre d'occurence"""
    liste = []
    for elem in set(text):
        liste.append((elem, text.count(elem)))
    return sorted(liste, key=lambda x : x[1])

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

def getDictText(text):
    """Donne le dictionnaire du code associé au texte"""
    return ArbreB.codage(ArbreB.create_tree(Sommet.make_list(comptage_lettre(text))))