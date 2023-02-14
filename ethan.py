def comptage_lettre(text):
    """prend une chaîne de caractère en entrée et renvoi
    une liste de tuplecontenant les lettres qui apparaissent
    dans le text et leur nombre d'occurence"""
    liste = []
    for elem in set(text):
        liste.append((elem, text.count(elem)))
    return sorted(liste, key=lambda x : x[1])

class ArbreB:
    def __init__(self, arbre):
        self.arbre = arbre

class Sommet(ArbreB):

    def __init__(self, arbre, parent, fd, fg, valeur, nom):
        self.parent = parent
        self.fd = fd
        self.fg = fg
        self.valeur = valeur
        self.nom = nom
        super().__init__(arbre)

    def affichage(self):
        print(self.parent, self.fd, self.fg, self.valeur, self.nom)

