# Auteurs du Projet :

- Sam Barbosa
- Ethan Mache

# Présentation Projet :

Le but du projet est de coder un texte selon le codage de Hauffman. Puis de crypter un texte selon le codage obtenu et ensuite de pouvoir le décrypter.


![Capture d'écran de mon application](Screenshot%202023-04-21%20at%2017.20.56.png)

# Mécanisme d'installation :

### Utilisation de l'application directement :

* Si vous êtes sur window double cliquer sur interface.exe
* Si vous êtes sur mac os double cliquer sur interface.dmg

### Autre solution en utilisant le code source directement

* Au préalable il faut installer python ainsi que les librairies tkinter, languedetect et math (pip install...)
* Dans le terminal tapez "python interface.py"

# Guide d'utilisation de l'application :

En haut à gauche un menu déroulant "choix langues" qui permet de choisir la langue. Saisissez la langue de votre choix.
(Français, anglais, allemand, espagnol, chinois)

![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2017.26.41.png)


### Pour obtenir un codage :
- Soit vous entrer du texte dans la boîte de texte soit vous cliquer sur le bouton "ouvrir un fichier pour obtenir un ocdage" ensuite si vous voulez voir le codage appuyer sur afficher le code.
![Capture d'écran de mon application](Screenshot%202023-04-21%20at%2017.47.25.png)

### Pour crypter un texte : 
- Soit vous entrer du texte dans la boîte de texte et appuyer sur le bouton "crypter"
- Soit vous cliquer sur le bouton "ouvrir un fichier à crypter"
![Capture d'écran de mon application](Screenshot%202023-04-21%20at%2017.47.32.png)


ATTENTION !!
- Si la langue est différente du texte où le codage a été fait, il y aura un message "ce n'est pas la meme langue"
- S’il y a un caractère dans le texte qui n'a pas de code, il y aura un message d'erreur "le caractère .... n'est pas dans le texte"

### Pour décrypter un texte : 
- Soit vous entrer du texte dans la boîte de texte et appuyer sur le bouton "décrypter"
- Soit vous cliquer sur le bouton "ouvrir un fichier à décrypter"
![Capture d'écran de mon application](Screenshot%202023-04-21%20at%2017.47.47.png)


# Architecture :

- Quand un texte est écrit dans la section codage et que le bouton Générer le code est pressé, le bouton va effacer le canvas, créer un nouvel arbre avec comme texte le résultat de la fonction comptage_lettre qui va compter les occurrences de chaque lettre, puis être transformé en une liste de Sommets 
grâce à la fonction make_list() de la classe Sommet pour enfin renvoyer l'arbre résultant de ArbreB.create_tree() 
- Le texte va être analysé pour connaître sa langue et changer la langue de la fenêtre si besoin.
- L'ArbreB va ensuite être dessiné dans le canvas et débloquer les boutons suivants.
- Une fois le code généré il est possible de le sauvegarder, de crypter un texte de même langue ou de décrypter un texte tout en vérifiant s'il a été codé selon le code généré (pas de message affiché si c'est le bon), une fois crypter ou décrypter pressé il est possible de sauvegarder ce résultat.
- L'ArbreB de codage peut-être modifié à tout moment il suffira de re cliquer sur le bouton Générer le code et d'actualiser au besoin les autres résultats en appuyant de nouveau sur les boutons.
- L'interface propose aussi un bouton permettant d'afficher et de désafficher le dictionnaire de codage, si le dictionnaire est trop grand il est préférable de le cacher pour que la taille de la fenêtre ne soit pas trop impactée.
- Il est aussi possible d'ouvrir des fichiers textes pour les lires ou les décrypter.
- Un bouton choix de langue est situé en haut à gauche de la fenêtre pour changer la langue de la fenêtre parmi Français, Anglais, Espagnol, Allemand ou Chinois.


# Explication du code :

## Librairies utilisées:

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
 * La classe possède la fonction make_list qui prend en entrée une liste de tuple (lettre, occurrence) et renvoie une liste contenant les Sommets de ces tuples.


## Interface (interface.py):



 #### La fonction comptage lettre :

 

 * Prends une chaîne de caractères en entrée et renvoi une liste de tuple contenant les lettres q

 *  on crée un ensemble  avec le text (set(text)) puis on itère dand cete ensemble chaque element un par un on ajoute chaque element à un dictionnaire ainsi que sa fréquence dans le text.

 

 #### La fonction getDictText :

 * Donne le dictionnaire du code associé au texte



 #### La fonction code_texte :

 * La fonction prend en argument un dictionnaire et un texte saisi par l'utilisateur. La fonction renvoie un texte crypté selon le dictionnaire si la langue des deux textes est la même sinon elle renvoie un message 'ce n'est pas la meme langue'.



 #### La fonction decrypte_texte :

 * La fonction prend en argument un dictionnaire et un texte saisie par l'utilisateur. La fonction renvoie un texte décrypté selon le dictionnaire.



 #### La fonction dessin :

 * La fonction dessin() prend en argument un canvas et un ArbreB. La fonction va dans un premier temps calculer la profondeur de l'ArbreB + 1 puis sa largeur, le nombre de nœuds dans l'ArbreB, ainsi qu'un coefficient qui va plus ou moins espacer les branches en fonction de si l'ArbreB est considéré comme grand, l'ArbreB est considéré grand quand la largeur^log2(profondeur) de l'ArbreB est supérieure à 90 (aux alentours d'une largeur de 6 et de profondeur 6). La fonction va ensuite calculer la position X du point suivant en partie grâce au coefficient et va calculer une taille minimale des positions pour pouvoir ajuster la zone de la scrollbar. Pour enfin envoyer ses calculs à la méthode dessinerArbre de la classe ArbreB en paramètre.



 #### La fonction effacer_canvas :

 * La fonction prend en argument un canvas. Elle permet d'effacer les éléments dans le canvas.



 #### La fonction language :

 * La fonction prend en argument la langue. Elle permet de changer la langue selon la langue choisie par l'utilisateur.



 #### La fonction afficher_dico :

 * La fonction ne prend pas d'argument. Elle permet d'afficher le dictionnaire contenant le codage dans la fenêtre graphique.



 #### La fonction verfi_lang :

 * La fonction ne prend pas d'argument. Elle permet de connaître la langue du texte où les statistiques sont faites et la langue du texte à   crypter. ELle renvoie Vrai si la langue est la même sinon elle renvoie Faux.



 #### La fonction open_file :

 * La fonction ne prend pas d'argument. Elle permet d'ouvrir un fichier pour obtenir un texte.



 #### La fonction  create_file :

 * La fonction ne prend pas d'argument. Elle permet de créer un fichier.



 #### La focntion save_text :

 * La fonction prend en argument un texte. Elle permet de sauvegarder le cryptage/décryptage d'un texte.

