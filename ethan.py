def comptage_lettre(text):
    """prend une chaîne de caractère en entrée et renvoi
    une liste de tuplecontenant les lettres qui apparaissent
    dans le text et leur nombre d'occurence"""
    liste = []
    for elem in set(text):
        liste.append((elem, text.count(elem)))
    return sorted(liste, key=lambda x : x[1])

class ArbreB(object):
    def __init__(self, racine=None):
        self.racine = racine

    def recherche(self, nom):
        """Prend un ArbreB en entré ainsi qu'un nom de Sommet à rechercher dans l'arbre
        et renvois le Sommet correspondant ou None sinon"""
        def recherche_sommet(self, nom):
            if type(self) == ArbreB:
                self = self.racine
            if self.nom == nom:
                return self
            elif self.fils_gauche != None and self.fils_droit != None:
                return recherche_sommet(self.fils_gauche, nom) or recherche_sommet(self.fils_droit, nom)
        return recherche_sommet(self, nom)
        

    def fusion_arbre(self, sommet1, sommet2):
        """Prend deux Sommet en entré et renvois un nouveau Sommet qui est le père des deux Sommets
        avec les valeurs des deux combinner"""
        return Sommet(sommet1.valeur + sommet2.valeur, sommet1.nom + sommet2.nom, sommet1, sommet2)
    
    def parcour_arbre(self):  # Inutile pour le moment et surrement plus tard
        def parcour_profondeur(self):
            if type(self) == ArbreB:
                self = self.racine
            if self.fils_gauche != None and self.fils_droit != None:
                return parcour_profondeur(self.fils_gauche), parcour_profondeur(self.fils_droit)
        parcour_profondeur(self)

    def create_tree(liste_sommet):
        """Prend une liste de Sommet en entré et retourne un objet ArbreB dont la racine est le sommet de plus haute valeur"""
        for _ in range(len(liste_sommet)-1):
            liste_sommet[0] = ArbreB.fusion_arbre(ArbreB, liste_sommet[0], liste_sommet[1])
            del liste_sommet[1]
            liste_sommet = sorted(liste_sommet, key=lambda x : x.valeur)
        return ArbreB(liste_sommet[0])
    
    def codage_arbre(self):
        """Prend un ArbreB en entré et renvois le code de Huffman
        de cet arbre sous forme de dictionnaire {nom_de_la_lettre : code_de_la_lettre}"""
        dico = {}
        def codage(self, code_sommet=""):
            if type(self) == ArbreB:
                self = self.racine
            if self.fils_gauche != None:
                codage(self.fils_gauche, code_sommet+"0")
            if self.fils_droit != None:
                codage(self.fils_droit, code_sommet+"1")
            if len(self.nom) == 1:
                dico[self.nom] = code_sommet
            return dico
        codage(self)
        return dico
    
class Sommet(object):

    def __init__(self, valeur, nom, fils_gauche=None, fils_droit=None):
        self.valeur = valeur
        self.nom = nom
        self.fils_droit = fils_droit
        self.fils_gauche = fils_gauche

    def affichage(self):
        return self.valeur, self.nom, self.fils_droit, self.fils_gauche

    def rename_sommet(self, new_name):
        self.nom = new_name

    def insertion_sommet(self, valeur, nom, liste_sommet):
        liste_sommet.append(Sommet(valeur, nom))
        return liste_sommet
    
    def suppression_sommet(self, liste_sommet):
        liste_sommet.remove(self)
        return liste_sommet
        
    def make_list(liste_occurence):
        """Prend en entré une liste de tuple (lettre, occurence) et renvois une liste contenant les Sommets de ces tuples"""
        liste_sommet = []
        for nom, valeur in liste_occurence:
            liste_sommet.append(Sommet(valeur, nom))
        return liste_sommet




test = comptage_lettre("bonjour")
#print(test)
l = Sommet.make_list(test)
#print(l)


a = ArbreB.create_tree(l)
#cd = ArbreB.codage_arbre(a)
#print(a.racine.affichage())
#print(a.racine.fils_gauche.affichage(), a.racine.fils_droit.affichage())
#print(a.racine.fils_gauche.fils_gauche.affichage(), a.racine.fils_gauche.fils_droit.fils_gauche.affichage(), a.racine.fils_gauche.fils_droit.fils_droit.affichage(), a.racine.fils_droit.fils_droit.affichage())

print(test)