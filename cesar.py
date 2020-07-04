"""
le chiffrement de cesar est une technique qui consiste a effectuer un decalage
des lettres de l'alphabet modulo 26 (l'ensemble des lettres de l'alphabet anglais)
"""
def chiffre_nombre(n,k):
	return (n+k)%26
	
def chiffre_message(message,k):
	message_crypte = []
	for caractere in message:
		if caractere == " ":
			caractere_crypte = caractere
		else:
			caractere = caractere.upper()
			char2int = ord(caractere) - 65 #de caractere -> entier
			char2int_crypte = chiffre_nombre(char2int,k)#entier -> entier chiffre
			caractere_crypte = chr(char2int_crypte + 65)#entier chiffré -> caractere crypté
		message_crypte.append(caractere_crypte)
	message_crypte = "".join(message_crypte)#liste -> chaine 
	return (message_crypte)

