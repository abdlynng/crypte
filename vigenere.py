"""
implementation de la methode de chiffrement par Vigenere. Il consiste a diviser le message en des blocs 
de taille k. La clé sera constitué de k nombres compris entre 0 et 25 (c1,c2,...,ck). Ensuite on applique 
le chiffrement de Cesar sur chaque bloc a partir de la clé. Ce qui fait que le chiffrement d'une lettre 
peut changer d'un bloc a un autre. 
@author : Abdoulaye NIANG
"""

#on compte la taille de chaque mot dans le message
def taille_mot(message):
    taille = []
    texte = message.split(" ")
    for i in range (0, len(texte)):
        taille.insert(i,len(texte[i]))
    return taille

# decoupage du message en des bloc de taille k
def decoupage_bloc(message, k):
    texte = "".join(message.split(" "))
    blocs = []
    #initialiser les blocs 
    blocs.insert(0,texte[0:k])
    i = 1  #indice de la liste 
    n = k
    while(n < len(texte) and  i <= (len(texte) // k) ):
        if ((n + k) > len(texte)):
            blocs.insert(i,texte[i*k:])
        else:
            blocs.insert(i,texte[n:n+k])
        i = i+1
        n = n+k   
    return blocs
import cesar 
def chiffre_message(message,cle):
    blocs = decoupage_bloc(message,len(cle))
    blocs_crypte = []
    
    for bloc in blocs:
        bloc_crypte = []
        tempon = []
        for i in range(0,len(bloc)):
            tempon.append(cesar.chiffre_message(bloc[i],cle[i])) 
        bloc_crypte = "".join(tempon)
        blocs_crypte.append(bloc_crypte)
    return blocs_crypte

def dechiffre_blocs(message, cle):
    blocs = message.split(" ")
    blocs_decrypte = []
    for bloc in blocs:
        bloc_decrypte = []
        for i in range(0,len(bloc)):
            bloc_decrypte.append(cesar.dechiffre_message(bloc[i], cle[i]))
        blocs_decrypte.append("".join(bloc_decrypte))
    return blocs_decrypte 