def comptage_lettre(text):
    """prend une chaîne de caractère en entrée et renvoi
    une liste de tuplecontenant les lettres qui apparaissent
    dans le text et leur nombre d'occurence"""
    liste = []
    for elem in set(text):
        liste.append((elem, text.count(elem)))
    return sorted(liste, key=lambda x : x[1])

class Sommet(object):

    def __init__(self, valeur, nom, fils_droit=None, fils_gauche=None):
        self.valeur = valeur
        self.nom = nom
        self.fils_droit = fils_droit
        self.fils_gauche = fils_gauche

    def affichage(self):
        return self.valeur, self.nom, self.fils_droit, self.fils_gauche

    def rename_sommet(self, new_name):
        self.nom = new_name


class ArbreB(object):
    def __init__(self, racine=None):
        self.racine = racine

    def suppression_sommet(self):
        pass

    def recherche_sommet(self):
        pass

    def fusion_arbre(self, sommet1, sommet2):
        return Sommet(sommet1.valeur + sommet2.valeur, sommet1.nom + sommet2.nom, sommet1, sommet2)



test = comptage_lettre("bonjour comment ca va ?")
print(test)
l = []
for nom, val in test:
    l.append(Sommet(val, nom))
#for i in range(len(l)):
#    l[i].affichage()

#l[-1].rename_sommet("test")
#l[-1].affichage()

l[0] = ArbreB.fusion_arbre(ArbreB, l[0], l[1])
del l[1]
print(l[0].affichage())
print(l[1].affichage())
