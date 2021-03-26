# IMPORT
import random
import os

# VARIABLES
comp_nbr = True
go_start = True
go = ''
liste = []


# FONCTIONS
def Choisir_nbr():
	nbr_str = input('Choisisser un nombre entre 0 et 100 ')
	nbr = int(nbr_str)
	return (nbr)


def Comparaison(nbr, comp_nbr):
	erreur = 0
	while comp_nbr == True:
		if nbr > rand_nbr:
			print('Moins')
		elif nbr < rand_nbr:
			print('Plus')
		erreur = erreur + 1
		nbr = Choisir_nbr()
		comp_nbr = nbr != rand_nbr
	else:
		print('Gagné !')
		print(erreur, ' erreurs')
	liste.append(str(erreur))
	print(liste)


def Read_score():
	highscore = open(
	  "Highscore.txt",
	  "r+",
	)
	liste_str = highscore.read()
	listef = liste_str.split()
	return (listef)


def Write_score():
	highscore = open(
    "Highscore.txt",
    "a+",
	)
	liste_str = '\n'.join(liste)
	highscore.write(liste_str + '\n')
	highscore.close()

def Get_rand_nbr():
	rand_nbr = os.getenv("TEST_RAND_NBR")
	if rand_nbr == "":
		rand_nbr = random.randint(0, 100)
	else:
		rand_nbr = int(rand_nbr)
	print(rand_nbr)
	return rand_nbr


# MAIN
listef = Read_score()
while go_start == True:
	rand_nbr = Get_rand_nbr()

	#pseudo = input('Quel est votre pseudo ? ')

	nbr = Choisir_nbr()
	comp_nbr = nbr != rand_nbr

	Comparaison(nbr, comp_nbr)

	go = input('Voulez-vous continuer ? ("o/n") ')
	go_start = go == 'o'

listef = listef + liste
listef = sorted(listef)

#for x in range(len(listef) - 1):
#	listef.append('Top ' + str(x))
#	print(listef)

print('Vos 3 meilleur score sont : ', listef[0], listef[1], listef[2])

Write_score()
