"""
le chiffrement de cesar est une technique qui consiste a effectuer un decalage
des lettres de l'alphabet modulo 26 (l'ensemble des lettres de l'alphabet anglais)
"""
def chiffre_nombre(n,k):
	return (n+k)%93 #reference de la 33 a la 126 caractere du code ascii
	
def chiffre_message(message,k):
	message_crypte = []
	for caractere in message:
		if caractere == " " or caractere == "\t" or caractere =="\n":
			caractere_crypte = caractere
		else:
			char2int = ord(caractere) - 33 #de caractere -> entier
			char2int_crypte = chiffre_nombre(char2int,k)#entier -> entier chiffre
			caractere_crypte = chr(char2int_crypte + 33)#entier chiffré -> caractere crypté
		message_crypte.append(caractere_crypte)
	message_crypte = "".join(message_crypte)#liste -> chaine 
	return (message_crypte)

#dechiffrement de message 

def dechiffre_nombre(n,k):
	return (n-k)%93
	
def dechiffre_message(message, k):
	message_decrypte = []
	for caractere in message:
		if caractere == " " or caractere == "\t" or caractere =="\n":
			caractere_decrypte = caractere
		else:
			char2int = ord(caractere) - 33
			char2int_decrypte = dechiffre_nombre(char2int, k)
			caractere_decrypte = chr(char2int_decrypte + 33)
		message_decrypte.append(caractere_decrypte)
	message_decrypte = "".join(message_decrypte)
	return (message_decrypte)

def chiffre_fichier(fichier_clair, k, fichier_crypte):
    f = open(fichier_clair,"r")
    d = open(fichier_crypte, "w")
    for ligne in f :
        d.write(chiffre_message(ligne,k))
    f.close()
    d.close()

def dechiffre_fichier(fichier_crypte, k, fichier_clair):
    f = open(fichier_crypte,"r")
    d = open(fichier_clair, "w")
    for ligne in f :
        d.write(dechiffre_message(ligne,k))
    f.close()
    d.close()