# Auteurs du Projet:

- Sam Barbosa
- Ethan Mache


# Présentation Projet :

Le but du projet est de coder un texte selon le codage de Hauffman. Puis de crypter un text selon le codage obtenu et ensuite de de pourvoir le décrypter.


![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2016.39.08.png)


# Guide d'utilisation de l'application :

En haut à gauche un menu déroulant "choix langues" qui permet de choisir la langue. Saississez la langue de votre choix.
(francais, anglais, allemand, espagnol, chinnois)

![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2017.26.41.png)



## Pour obtenir un codage :
- soit vous entrer du text dans la boite de texte soit vous cliquer sur le button "ouvrir un fichier pour obtenir un ocdage" ensuite si vous voulez voir le codage appuyer sur afficher le code.
![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2017.49.18.png)

## Pour crypter un text : 
- soit vous entrer du text dans la boite de texte et appuyer sur le bouton "crypter"
- soit vous cliquer sur le button "ouvrir un fichier à crypter"
![Capture d'écran de mon application](Screenshot%202023-04-20%20at%2017.49.29.png)


ATTENTION !!
- si la langue est différente du texte où le codage a été fait, il y aura un message "ce n'est pas la meme langue"
- si il y a un caractère dans le text qui n'a pas de code, il y aura un message d'erreur "le caractère .... n'est pas dans le text"

Pour décrypter un text : 
- soit vous entrer du text dans la boite de texte et appuyer sur le bouton "décrypter"
- soit vous cliquer sur le button "ouvrir un fichier à décrypter"
![Capture d'écran de mon application]
ATTENTION !!
- si ...


# Explication du code :

### Librairie utilisés:

- tkinter
- maths
- languedetect


### Module arbre (ethan.py):

Création de deux classes Sommet et Arbre.

ethan fait cette partie :)

### Interface (interface.py):

 - la fonction "comptage lettre"prend une chaîne de caractère en entrée et renvoi une liste de tuple contenant les lettres qui apparaissent dans le  text et leur nombre d'occurence.
 * on créer un ensemble  avec le text (set(text)) puis on itère dand cete ensemble chaque element un par un on ajoute chaque element à un dictionnaire ainsi que sa fréquence dans le text.
 



