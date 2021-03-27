#! /usr/bin/env python3

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


def Comparaison(nbr, comp_nbr, pseudo):
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
	liste.append((pseudo, str(erreur)))
	print(liste)


def Read_score():
	highscore = open(
	  "Highscore.txt",
	  "r+",
	)
	liste_str = highscore.read()
	listef = liste_str.split('\n')
	listef = list(filter(lambda x: x != '', listef))
	listef = list(map(lambda x: x.split(' '), listef))
	listef = list(map(lambda x: tuple(x), listef))

	return (listef)


def Write_score():
	highscore = open(
    "Highscore.txt",
    "a+",
	)
	liste_str = list(map(lambda x: x[0] + ' ' + str(x[1]), liste))
	liste_str =	'\n'.join(liste_str)
	highscore.write(liste_str + '\n')
	highscore.close()

def Get_rand_nbr():
	rand_nbr = os.getenv("TEST_RAND_NBR")
	if rand_nbr == None:
		rand_nbr = random.randint(0, 100)
	else:
		rand_nbr = int(rand_nbr)
	print(rand_nbr)
	return rand_nbr

def Show_score():
	xx = []
	for x in range(0, 3):
		xx.append(' : '.join(listef[x]))  
	print('Les 3 meilleur score sont : ', *xx)



# MAIN
listef = Read_score()
while go_start == True:
	rand_nbr = Get_rand_nbr()

	pseudo = input('Quel est votre pseudo ? ')

	nbr = Choisir_nbr()
	comp_nbr = nbr != rand_nbr

	Comparaison(nbr, comp_nbr, pseudo)

	go = input('Voulez-vous continuer ? ("o/n") ')
	go_start = go == 'o'

listef = listef + liste
print(listef)

listef = sorted(listef, key=lambda x: x[1])

for x in range(len(listef) + 1, 4):
	listef.append(('Top', str(x)))
	print(listef)


Show_score()
Write_score()
