import math
class ArbreB(object):
    def __init__(self, racine=None):
        self.racine = racine

    def getRacine(self):
        return self.racine
    def setRacine(self, nouvRacine):
        self.racine = nouvRacine

    def recherche_sommet(self, nom):
        """
        Prend un ArbreB et appel la fonction sur sa racine qui est un Sommet
        """
        if type(self) == ArbreB:
            return self.getRacine().recherche_sommet(nom)

    def fusion_arbre(self, sommet1, sommet2):
        """
        Prend deux Sommet en entré et renvois un nouveau Sommet qui est le père des deux Sommets
        avec les valeurs des deux combinner
        """
        return Sommet(sommet1.valeur + sommet2.valeur, sommet1.nom + sommet2.nom, sommet1, sommet2)
    
    def profondeur_arbre(self, profondeur=0):
        """
        Prend un ArbreB en entré et retourne sa profondeur maximale
        """
        if type(self) == ArbreB:
            self = self.getRacine()
        if self.getGauche() != None and self.getDroit() != None:
            profondeur = max(self.getGauche().profondeur_arbre(profondeur+1), self.getDroit().profondeur_arbre(profondeur+1))
        return profondeur
    
    def largeur_arbre(self):
        """
        Prend un ArbreB en entré en retourne sa largeur totale, sa largeur à gauche et sa largeur à droite
        """
        if type(self) == ArbreB:
            self = self.getRacine()
        dico = self.codage()
        list_key = list(dico.values())
        return len(list_key[0]) + len(list_key[-1]), len(list_key[0]), len(list_key[-1])

    def create_tree(liste_sommet):
        """
        Prend une liste de Sommet en entré et retourne un objet ArbreB dont la racine est le sommet de plus haute valeur
        """
        if len(liste_sommet) < 2:
            raise "il doit y avoir 2 ou plus caractères différents"
        for _ in range(len(liste_sommet)-1):
            liste_sommet[0] = ArbreB.fusion_arbre(ArbreB, liste_sommet[0], liste_sommet[1])
            del liste_sommet[1]
            liste_sommet = sorted(liste_sommet, key=lambda x : x.valeur)
        return ArbreB(liste_sommet[0])
    
    def codage(self, code_sommet="", dico={}, all=False):
        """
        Prend un ArbreB et appel la fonction sur sa racine qui est un Sommet
        """
        if type(self) == ArbreB:
            return self.racine.codage(code_sommet, dico, all)
        
    def insertion_sommet(self, valeur, nom, liste_sommet):
        liste_sommet.append(Sommet(valeur, nom))
        return ArbreB.create_tree(liste_sommet)

    def suppression_sommet(self, nom, liste_sommet):
        """
        
        """
        liste_sommet.remove(self.recherche_sommet(nom))
        return ArbreB.create_tree(liste_sommet)
    
    def dessinerArbre(self, canvas, largeur_canvas, x=0, y=0, cpt=1, largeur=0, profondeur=0, taille=[0, 0], posXSuivant=0):
        """
        Prend un ArbreB et appel la fonction sur sa racine qui est un Sommet
        """
        if type(self) == ArbreB:
            self = self.getRacine()
        self.dessinerArbre(canvas, largeur_canvas, x, y, cpt, largeur, profondeur, taille, posXSuivant)

    def nb_noeud(self):
        """
        Prend un ArbreB et appel la fonction sur sa racine qui est un Sommet
        """
        if type(self) == ArbreB:
            return self.getRacine().nb_noeud()
    

class Sommet(ArbreB):
    def __init__(self, valeur, nom, fils_gauche=None, fils_droit=None):
        self.valeur = valeur
        self.nom = nom
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit

    def getValeur(self):
        return self.valeur
    def setValeur(self, newValeur):
        self.valeur = newValeur
    def getNom(self):
        return self.nom
    def setNom(self, newNom):
        self.nom = newNom
    def getGauche(self):
        return self.fils_gauche
    def setGauche(self, newGauche):
        self.fils_gauche = newGauche
    def getDroit(self):
        return self.fils_droit
    def setGauche(self, newDroit):
        self.fils_droit = newDroit

    def __str__(self):
        """
        Prend un Sommet et permet d'afficher sa valeur, son nom, son fils gauche et son fils droit
        """
        return f"{self.getValeur(), self.getNom(), self.getGauche(), self.getDroit()}"
    
        
    def make_list(liste_occurence : list):
        """
        Prend en entré une liste de tuple (lettre, occurence) et renvois une liste contenant les Sommets de ces tuples
        """
        liste_sommet = []
        for nom, valeur in liste_occurence:
            liste_sommet.append(Sommet(valeur, nom))
        return liste_sommet

    def make_list2(dict_occurence : dict):
        """
        Prend en entré un dictionnaire (lettre, occurence) et renvois une liste contenant les Sommets de ces tuples
        """
        liste_sommet = []
        for nom, valeur in dict_occurence.items():
            liste_sommet.append(Sommet(valeur, nom))
        return liste_sommet

    def codage(self, code_sommet="", dico={}, all=False):
        """
        La fonction prend un Sommet et retourne un dictionnaire contenant le code d'Huffman associer
        """
        if self.getGauche() != None:
            self.getGauche().codage(code_sommet+"0", dico, all)
        if self.getDroit() != None:
            self.getDroit().codage(code_sommet+"1", dico, all)
        if len(self.getNom()) == 1 and all == False:
            dico[self.getNom()] = code_sommet
        if all != False:
            dico[self.getNom()] = code_sommet 
        return dico
    
    def recherche_sommet(self, nom):
            """
            La fonction prend en argument un nom de sommet et renvoie le Sommet si il est dans l'arbre sison None
            """
            if self.getNom() == nom:
                return self
            elif self.getGauche() != None and self.getDroit() != None:
                return self.getGauche().recherche_sommet(nom) or self.getDroit().recherche_sommet(nom)
            else:
                return None

    def dessinerArbre(self, canvas, largeur_canvas, x=0, y=0, cpt=1, largeur=0, profondeur=0, taille=[0, 0], posXSuivant=0):
        """
        La fonction prend en argument un canvas, sa largeur, une position de départ x et y, la profondeur de l'arbre
        une taille de qui permet de mettre à jour la scrollbar et la position X de point suivant
        """
        posYSuivant = largeur_canvas // profondeur * cpt
        if self.getGauche() == None and self.getDroit() == None:
            color = "royalblue"
        else:
            color = "red"
            canvas.create_line(x, y, x-posXSuivant, posYSuivant, arrow="last", fill="black")
            canvas.create_line(x, y, x+posXSuivant, posYSuivant, arrow="last", fill="black")
        canvas.create_oval(x-10, y, x+10, y+20, fill=color)
        canvas.create_text(x, y+15, text=self.getNom(), fill="black")
        canvas.config(scrollregion=(-taille[0], 0, taille[1], 0))
        if self.getGauche() != None and self.getDroit() != None:
            self.getGauche().dessinerArbre(canvas, largeur_canvas, x-posXSuivant, posYSuivant, cpt+1, largeur, profondeur, taille, posXSuivant/2)
            self.getDroit().dessinerArbre(canvas, largeur_canvas, x+posXSuivant, posYSuivant, cpt+1, largeur, profondeur, taille, posXSuivant/2)

    def nb_noeud(self, nb=1):
        """
        La fonction renvoie le nombre de noeuds de l'arbre + 1
        """
        nb += 1
        if self.getGauche() != None and self.getDroit() != None:
            return self.getGauche().nb_noeud() + self.getDroit().nb_noeud()
        return nb
 
