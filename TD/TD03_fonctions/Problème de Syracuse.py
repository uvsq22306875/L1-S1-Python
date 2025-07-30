def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    nb = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        nb.append(n)
    return nb

print(syracuse(3))



def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range (1, n_max+1):
        if syracuse(i)[-1] == 1 :
            continue
        else :
            return False
    return True

print(testeConjecture(10000))



def tempsVol(n):
    """ Retourne le temps de vol de n """
    return (len(syracuse(n))-1)

print("Le temps de vol de", 3, "est", tempsVol(3))



def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1,n_max+1)]
    
print(tempsVolListe(100))



liste_t = tempsVolListe(10000)
liste_t_max = max(liste_t)
print("l'entier", liste_t.index(liste_t_max)+1,"a le plus grand temps de vol égal à",liste_t_max)



def alt_max(n):
    return max(syracuse(n))
def alt_max_liste(n_max):
    return [alt_max(i) for i in range(1, n_max+1)]

liste_alt = alt_max_liste(10000)
altitude = max(liste_alt)
print("l'entier", liste_alt.index(altitude),"a la plus grande altitude qui est égal à",altitude)