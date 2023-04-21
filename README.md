# Auteurs du Projet:

- Sam Barbosa
- Ethan Mache

# Présentation Projet :

Le but du projet est de coder un texte selon le codage de Hauffman. Puis de crypter un text selon le codage obtenu et ensuite de de pourvoir le décrypter.


![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2016.39.08.png)

# Mécanisme d'installation :

### Utilisation de l'application directement :

* si vous êtes sur window double cliquer sur interface.exe
* si vous êtes sur mac os douvble cliquer sur interface.dmg

### Autre solution en utilisant le code source directement

* au préalable il faut installer python ainsi que les librairies tkinter, languedetect et math (pip install [librairie])
* dans le terminal tapez "python interface.py"

# Guide d'utilisation de l'application :

En haut à gauche un menu déroulant "choix langues" qui permet de choisir la langue. Saississez la langue de votre choix.
(francais, anglais, allemand, espagnol, chinnois)

![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2017.26.41.png)



### Pour obtenir un codage :
- soit vous entrer du text dans la boite de texte soit vous cliquer sur le button "ouvrir un fichier pour obtenir un ocdage" ensuite si vous voulez voir le codage appuyer sur afficher le code.
![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2017.49.18.png)

### Pour crypter un text : 
- soit vous entrer du text dans la boite de texte et appuyer sur le bouton "crypter"
- soit vous cliquer sur le button "ouvrir un fichier à crypter"
![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2017.49.29.png)


ATTENTION !!
- si la langue est différente du texte où le codage a été fait, il y aura un message "ce n'est pas la meme langue"
- si il y a un caractère dans le text qui n'a pas de code, il y aura un message d'erreur "le caractère .... n'est pas dans le text"

### Pour décrypter un text : 
- soit vous entrer du text dans la boite de texte et appuyer sur le bouton "décrypter"
- soit vous cliquer sur le button "ouvrir un fichier à décrypter"
![Capture d'écran de mon application]
ATTENTION !!
- si ...


# Explication du code :

## Librairie utilisés:

- tkinter
- maths
- languedetect


## Module arbre (module_arbre.py):

Création de deux classes Sommet et Arbre.

#### class ArbreB(Object) : 
 * Les objets de la classe ArbreB sont représentés par une racine qui est un Sommet.
 * La classe possède plusieurs méthodes permettant notamment de connaître la profondeur de l'ArbreB, sa largeur totale et celle à gauche et à droite.
 * Le calcul de la profondeur se fait par un appel récursif sur les noeuds de l'ArbreB tandis que la largeur se calcule à partir du dictionnaire de codage qui retient la longueur du chemin avec que des 0 (chemin de gauche) et le chemin avec des 1 (chemin de droite).
 * La classe permet aussi de rechercher un Sommet dans l'ArbreB à partir du nom du Sommet ou de son identifiant.
 * Il est possible de créer un ArbreB avec la fonction create_tree() qui prend un argument une liste de sommet et renvoi l'ArbreB de Huffman associé, pour ce faire, la fonction prends les deux plus petites valeurs des Sommets, les fusionnent et les remet dans la liste des Sommets.
 * La classe permet aussi d'obtenir le codage d'Huffman de l'ArbreB en le parcourant de manière récursive et en associant un 0 au code quand il s'agit d'un sous arbre-gauche et un 1 dans le cas d'un sous arbre-droit, la méthode renvoie un dictionnaire contenant le nom en clé et le code en valeur des feuilles de l'ArbreB ou de tout les Sommets.
 * Il est aussi possible d'insérer et de supprimer un Sommet dans l'ArbreB, de connaître le nombre de Sommets dans l'arbre.
 * La classe possède les méthodes getListeSommet et getListeFeuille qui donnent une liste avec tous les Sommets de l'ArbreB ou toutes les feuilles de l'ArbreB.
 * Et enfin il est possible de dessiner l'ArbreB avec la méthode dessinerArbre() qui va prendre en argument un canvas, la largeur du canvas, une position x et y de départ facultatifs, la largeur de l'arbre, sa profondeur et la position X du point suivant. À chaque appel de la méthode, on va regarder si le Sommet est une feuille pour changer sa couleur et ne pas dessiner de flèches vers ses fils et tant que le Sommet a des fils, on va rappeler la méthode.
 
#### class Sommet(ArbreB) :
 * Chaque objet de la classe Sommet est caractérisé par une valeur entière, un nom ainsi qu'un fils droit et un fils gauche qui sont des Sommets, si le Sommet n'a pas de fils gauche ou droit alors la valeur est None.
 * La classe Sommet hérite de la classe ArbreB pour pouvoir profiter de ses méthodes.
 * La classe possède la fonction make_list qui prends en entrée une liste de tuple (lettre, occurrence) et renvoie une liste contenant les Sommets de ces tuples.


## Interface (interface.py):

 #### La fonction comptage lettre :
 
 * prend une chaîne de caractère en entrée et renvoi une liste de tuple contenant les lettres qui apparaissent dans le  text et leur nombre d'occurence.
 *  on créer un ensemble  avec le text (set(text)) puis on itère dand cete ensemble chaque element un par un on ajoute chaque element à un dictionnaire ainsi que sa fréquence dans le text.
 
 #### La fonction getDictText :
 * Donne le dictionnaire du code associé au texte

 #### La fonction code_texte :
 * La fonction prend en argument un dictionnaire et un texte saisi par l'utilisateur. La fonction renvoie un texte crypté selon le dictionnaire si la langue des deux textes est la même sinon elle renvoie un message 'ce n'est pas la meme langue'.

 #### La fonction decrypte_texte :
 * La focntion prend en argument un dicctionnaire et un text saisie par l'utilisateur. La focntion renvoie un text decrypter selon le dictionnaire.

 #### La fonction dessin :
 * La fonction dessin() prend en argument un canvas et un ArbreB. La fonction va dans un premier temps calculer la profondeur de l'ArbreB + 1 puis sa largeur, le nombre de noeuds dans l'ArbreB, ainsi qu'un coefficient qui va plus ou moins espacer les branches en fonction de si l'ArbreB est considéré comme grand, l'ArbreB est considéré grand quand la largeur^log2(profondeur) de l'ArbreB est supérieure à 90 (aux alentours d'une largeur de 6 et de profondeur 6). La fonction va ensuite calculer la position X du point suivant en partie grâce au coefficient et va calculer une taille minimale des positions pour pouvoir ajuster la zone de la scrollbar. Pour enfin envoyer ses calculs à la méthode dessinerArbre de la classe ArbreB en paramètre.

 #### La fonction effacer_canvas :
 * La fonction prend en argument un canvas. Elle permet d'effacer les éléments dans le canvas.

 #### La fonction language :
 * La fonction prend en argument la langue. Elle permet de changer la langue selon la langue choisie par l'utilisateur.

 #### La fonction afficher_dico :
 * La fonction ne prend pas d'argument. Elle permet d'afficher le dictionnaire contenant le codage dans la fenetre graphique.

 #### La fonction verfi_lang :
 * La fonction ne prend pas d'argument. Elle permet de connaitre la langue du texte où les statitiques sont faites et la langue du texte à crypter. ELle renvoie Vrai si la langue est la meme sinon elle renvoie Faux.

 #### La fonction open_file :
 * La fonction ne prend pas d'argument. Elle permet d'ouvir un fichier pour obtenir un texte.

 #### La fonction  create_file :
 * La fonction ne prend pas d'argument. Elle permet de créer un fichier.

 #### La focntion save_text :
 * La fonction prend en argument un texte.
    Elle permet de sauvegarder le cryptage/decryptage d'un texte.
