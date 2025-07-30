carre_mag = [[4, 14, 15, 1],[9, 7, 6, 12],[5, 11, 10, 8],[16, 2, 3, 13]]
carre_pas_mag = []

for ligne in carre_mag:
    carre_pas_mag.append(ligne.copy())
carre_pas_mag[3][2] = 7


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre:
        print(ligne)
    print()

afficheCarre(carre_mag) 
afficheCarre(carre_pas_mag)



def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    sommeL = sum(carre[0])
    for ligne in carre :
        if sommeL != sum(ligne) :
            return -1
    return sommeL

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))



def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    colonne1 = [ligne[0] for ligne in carre]
    sommeC = sum(colonne1)
    for num_colonne in range(1, len(carre)):
        colonne = [ligne[num_colonne] for ligne in carre]
        if sum(colonne) != sommeC:
            return -1
    return sommeC

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))



def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    d1 = [carre[j][j] for j in range(len(carre))]
    d2 = [carre[i][len(carre) - 1 - i] for i in range(len(carre))]
    somme_d1 = sum(d1)
    if somme_d1 == sum(d2) :
        return somme_d1
    else : 
        return -1

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testLignesEgales(carre) == testColonnesEgales(carre) == testDiagonalesEgales(carre)

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))