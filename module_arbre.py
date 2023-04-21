class ArbreB(object):
    def __init__(self, racine=None):
        self.racine = racine


    def getRacine(self):
        return self.racine
    

    def setRacine(self, nouvRacine):
        self.racine = nouvRacine


    def profondeur_arbre(self, profondeur=0):
        """
        Prends un ArbreB en entrée et retourne sa profondeur maximale.
        """
        if type(self) == ArbreB:
            self = self.getRacine()
        if self.getGauche() != None and self.getDroit() != None:
            profondeur = max(self.getGauche().profondeur_arbre(profondeur+1), self.getDroit().profondeur_arbre(profondeur+1))
        return profondeur


    def largeur_arbre(self):
        """
        Prends un ArbreB en entrée en retourne sa largeur totale, sa largeur à gauche et sa largeur à droite.
        """
        if type(self) == ArbreB:
            self = self.getRacine()
        dico = self.codage()
        list_key = list(dico.values())
        return len(list_key[0]) + len(list_key[-1]), len(list_key[0]), len(list_key[-1])


    def recherche_sommet(self, nom, type_rec=None):
        """
        La méthode prend en argument un nom de Sommet ou un Sommet et renvoie le Sommet s'il est dans l'arbre sinon None.
        """
        if type(self) == ArbreB:
            self = self.getRacine()
            type_rec = type(nom)
            if type_rec == Sommet:
                return self.recherche_sommet(nom, Sommet)
            elif type_rec == str:
                return self.recherche_sommet(nom, str)
            else:
                raise TypeError("la valeur doit être un Sommet ou un str")
        if type_rec == str:
            if self.getNom() == nom:
                return self
            elif self.getGauche() != None and self.getDroit() != None:
                return self.getGauche().recherche_sommet(nom, type_rec) or self.getDroit().recherche_sommet(nom, type_rec)
            else:
                return None
        else:
            if self == nom:
                return self
            elif self.getGauche() != None and self.getDroit() != None:
                return self.getGauche().recherche_sommet(nom, type_rec) or self.getDroit().recherche_sommet(nom, type_rec)
            else:
                return None


    def fusion_sommet(self, sommet1, sommet2):
        """
        Prends deux Sommets en entrée et renvoie un nouveau Sommet qui est le père des deux Sommets
        avec les valeurs des deux combiné.
        """
        return Sommet(sommet1.valeur + sommet2.valeur, sommet1.nom + sommet2.nom, sommet1, sommet2)
    

    def fusion_arbre(self, autre_arbre):
        """
        Prends un ArbreB en entrée et retourne un arbre fusionné.
        """
        return ArbreB(Sommet(self.getRacine().getValeur() + autre_arbre.getRacine().getValeur(), self.getRacine().getNom() + autre_arbre.getRacine().getNom(),
                             self.getRacine(), autre_arbre.getRacine()))
    

    def decomposition_arbre(self):
        """
        Renvoie la liste des Sommets de l'arbre et supprime l'ArbreB.
        """
        liste = self.getListeFeuille()
        del self
        return liste


    def __add__(self, sommet1, sommet2):
        return self.fusion_sommet(sommet1, sommet2)


    def create_tree(liste_sommet):
        """
        Prends une liste de Sommet en entrée et retourne un objet ArbreB dont la racine est le sommet de plus haute valeur.
        """
        if len(liste_sommet) < 2:
            raise "Il doit y avoir 2 ou plus caractères différents pour avoir un arbre."
        for _ in range(len(liste_sommet)-1):
            liste_sommet[0] = ArbreB.fusion_sommet(ArbreB, liste_sommet[0], liste_sommet[1])
            del liste_sommet[1]
            liste_sommet = sorted(liste_sommet, key=lambda x : x.valeur)
        return ArbreB(liste_sommet[0])
    

    def codage(self, code_sommet="", dico={}, all=False):
        """
        La méthode prend un Sommet et retourne un dictionnaire contenant le code d'Huffman associer,
        la variable all permet d'obtenir le dictionnaire pour tous les Sommets de l'ArbreB.
        """
        if type(self) == ArbreB:
            return self.getRacine().codage(code_sommet, {}, all)
        if self.getGauche() != None:
            self.getGauche().codage(code_sommet+"0", dico, all)
        if self.getDroit() != None:
            self.getDroit().codage(code_sommet+"1", dico, all)
        if len(self.getNom()) == 1 and all == False:
            dico[self.getNom()] = code_sommet
        if all != False:
            dico[self.getNom()] = code_sommet
        return dico


    def insertion_sommet(self, sommet):
        """
        La méthode prend un ArbreB et un Sommet en argument et renvoi un nouvel arbre avec le Sommet inséré.
        """
        liste_sommet = self.getListeFeuille()
        liste_sommet.append(sommet)
        return ArbreB.create_tree(liste_sommet)
    

    def __iadd__(self, sommet):
        return self.insertion_sommet(sommet)


    def suppression_sommet(self, nom):
        """
        Prends en entrée un ArbreB, un nom de Sommet ou un Sommet et renvoi l'ArbreB sans ce sommet.
        """
        liste_sommet = self.getListeFeuille()
        find = self.recherche_sommet(nom)
        if find != None:
            liste_sommet.remove(find)
            return ArbreB.create_tree(liste_sommet)
        else:
            raise ValueError("Le sommet n'existe pas dans l'arbre")
        

    def  __isub__(self, nom):
        return self.suppression_sommet(nom)
    

    def dessinerArbre(self, canvas, largeur_canvas, x=0, y=0, cpt=1, largeur=0, profondeur=0, taille=[0, 0], posXSuivant=0):
        """
        La méthode prend en argument un canvas, sa largeur, une position de départ x et y, la profondeur de l'arbre,
        une taille qui permet de mettre à jour la scrollbar et la position X de point suivant.
        """
        if type(self) == ArbreB:
            self = self.getRacine()
            self.dessinerArbre(canvas, largeur_canvas, x, y, cpt, largeur, profondeur, taille, posXSuivant)
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
        La méthode renvoie le nombre de noeuds de l'arbre passé en argument + 1.
        """
        if type(self) == ArbreB:
            return self.getRacine().nb_noeud()
        nb += 1
        if self.getGauche() != None and self.getDroit() != None:
            return self.getGauche().nb_noeud() + self.getDroit().nb_noeud()
        return nb
        

    def getListeSommet(self, liste_sommet=[]):
        """
        Prends en argument un ArbreB et retourne une liste de tous ses Sommets.
        """
        if type(self) == ArbreB:
            return self.getRacine().getListeSommet([])
        if self.getGauche() != None and self.getDroit() != None:
            self.getGauche().getListeSommet(liste_sommet), self.getDroit().getListeSommet(liste_sommet)
        liste_sommet.append(self)
        return liste_sommet
        

    def getListeFeuille(self, liste_sommet=[]):
        """
        Prends en argument un ArbreB et retourne une liste de ses feuilles.
        """
        if type(self) == ArbreB:
            return self.getRacine().getListeFeuille([])
        if self.getGauche() != None and self.getDroit() != None:
            self.getGauche().getListeFeuille(liste_sommet), self.getDroit().getListeFeuille(liste_sommet)
        else:
            liste_sommet.append(self)
        return liste_sommet


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
        Prends un Sommet et permet d'afficher sa valeur, son nom, son fils gauche et son fils droit.
        """
        return f"{self.getValeur(), self.getNom(), self.getGauche(), self.getDroit()}"
    
        
    def make_list(liste_occurence):
        """
        Prends en entrée une liste de tuple (lettre, occurRence) et renvoie une liste contenant les Sommets de ces tuples.
        """
        liste_sommet = []
        for nom, valeur in liste_occurence:
            liste_sommet.append(Sommet(valeur, nom))
        return liste_sommet
