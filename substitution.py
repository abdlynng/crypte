"""
implementation de la methode de chiffrement par substitution 
Il consiste a faire correspondre chaque lettre de l'alphabet 
a une autre lettre sans regle definie (aleatoirement).
@author : Abdoulaye NIANG
"""
table = {
    'A':'V',\
    'B':'H',\
    'C':'K',\
    'D':'N',\
    'E':'F',\
    'F':'Q',\
    'G':'T',\
    'H':'W',\
    'I':'S',\
    'J':'M',\
    'K':'P',\
    'L':'A',\
    'M':'L',\
    'N':'G',\
    'O':'D',\
    'P':'R',\
    'Q':'Z',\
    'R':'B',\
    'S':'J',\
    'T':'Y',\
    'U':'E',\
    'V':'X',\
    'W':'C',\
    'X':'O',\
    'Y':'U',\
    'Z':'I'
    }

def chiffre_caractere(caractere):
    return table.get(caractere)

def chiffre_message(message):
    message_crypte = []
    for caractere in message:
        if caractere == " " or caractere == "\t" or caractere =="\n":
            caractere_crypte = caractere
        else:
            caractere = caractere.upper()
            caractere_crypte = chiffre_caractere(caractere)
        message_crypte.append(caractere_crypte)
    message_crypte = "".join(message_crypte)
    return message_crypte

#creation de la table de correspondance de decryptage par correspondance a celle de cryptage 
d_table = {}
for cle in table:
    d_table[table.get(cle)] = cle

def dechiffre_caractere(caractere):
    return d_table.get(caractere)

def dechiffre_message(message):
    message_decrypte = []
    for caractere in message:
        if caractere == " " or caractere == "\t" or caractere =="\n":
            caractere_decrypte = caractere
        else:
            caractere = caractere.upper()
            caractere_decrypte = dechiffre_caractere(caractere)
        message_decrypte.append(caractere_decrypte)
    message_decrypte = "".join(message_decrypte)
    return message_decrypte