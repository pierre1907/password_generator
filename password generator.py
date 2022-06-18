import string
import random


## caractères à partir desquels générer le mot de passe
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## Longueur du mot de passe de l'utilisateur
	length = int(input("Entrez la longueur du mot de passe : "))

	## Nombre de types de caractères
	alphabets_count = int(input("Entrez le nombre de lettres du mot de passe: "))
	digits_count = int(input("Entrez le nombre de chiffres dumot de passe : "))
	special_characters_count = int(input("Entrez le nombre de caratères spéciaux du mot de passe : "))

	characters_count = alphabets_count + digits_count + special_characters_count

	## vérifier la longueur totale avec le nombre de caractères
    ## Affichage non valide si la somme est supérieure à la longueur
    if characters_count > length:
		print("Le nombre total de caractères est supérieur à la longueur du mot de passe")
		return


	## Initialisation du mot de passe
	password = []

	## Choix des lettres au hasard
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	## Choix des chiffres au hasard
	for i in range(digits_count):
		password.append(random.choice(digits))


	## Choix des caratères spéciaux au hasard
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	## si le nombre total de caractères est inférieur à la longueur du mot de passe
    ## ajouter des caractères aléatoires pour le rendre égal à la longueur
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	## mélanger le mot de passe résultant
	random.shuffle(password)

	## convertir la liste en chaîne
    ## impression de la liste
	print("Le mot de passe est : ".join(password))

	print(password)

## Invocation de la fonction
generate_random_password()