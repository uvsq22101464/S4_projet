def comptage_lettre(text):
    """prend une chaîne de caractère en entrée et renvoi
    une liste de tuplecontenant les lettres qui apparaissent
    dans le text et leur nombre d'occurence"""
    liste = []
    for elem in set(text):
        liste.append((elem, text.count(elem)))
    return sorted(liste, key=lambda x : x[1])

class ArbreB(object):
    def __init__(self, racine, nb_sommet):
        self.racine = racine
        self.nb_sommet = nb_sommet

    def insertion_sommet(self):
        pass

    def suppression_sommet(self):
        pass

    def recherche_sommet(self):
        pass

    def fusion_arbre(self):
        pass

class Sommet(ArbreB):

    def __init__(self, valeur, nom, racine="self", nb_sommet=1):
        super().__init__(racine, nb_sommet)
        self.valeur = valeur
        self.nom = nom

    def affichage(self):
        print(self.valeur, self.nom)

    def rename_sommet(self, new_name):
        self.nom = new_name

test = comptage_lettre("bonjour comment ca va ?")
print(test)
l = []
for elem in test:
    l.append(Sommet(elem[1], elem[0]))
for i in range(len(l)):
    l[i].affichage()

#l[-1].rename_sommet("test")
#l[-1].affichage()