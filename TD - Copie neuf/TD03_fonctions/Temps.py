def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps [0]*24*60*60 + temps[1]*60*60 + temps[2]*60 + temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // (60*60*24)
    reste = seconde % (60*60*24)
    heure = reste // (60*60)
    reste1 = reste % (60*60)
    minute = reste1 // 60
    seconde = reste1 % 60
    return (jour,heure,minute,seconde)

temps = secondeEnTemps(100000)
print (secondeEnTemps(100000))
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")



def mot_pluriel(mot,nombre):
    if nombre > 0 :
        print("", nombre, mot, end="")
    if nombre > 1 :
        print("s", end="")

def afficheTemps(temps):
    mot_pluriel("jour",temps[0])
    mot_pluriel("heure",temps[1])
    mot_pluriel("minute",temps[2])
    mot_pluriel("seconde",temps[3])
    print()
    
afficheTemps((1,0,14,23))



def demandeTemps():
    jour = -1
    while (jour < 0) :
        jour = int(input())
    heure = -1
    while (heure < 0 or heure >=24) :
        heure = int(input())
    minute = -1
    while (minute < 0 or minute >=60) :
        minute = int(input())
    seconde = -1
    while (seconde < 0 or seconde >=60) :
        seconde = int(input())
    return (jour,heure,minute,seconde)

afficheTemps(demandeTemps())



def sommeTemps(temps1,temps2):
    return secondeEnTemps(tempsEnSeconde(temps1)+tempsEnSeconde(temps2))

afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))



def proportionTemps(temps,proportion):
    int(tempsEnSeconde(temps)*proportion)
    return secondeEnTemps(int(tempsEnSeconde(temps)*proportion))

afficheTemps(proportionTemps((2,0,36,0),0.2))



def tempsEnDate(temps):
    année = 1970 + (temps[0]//365)
    nb_jours = temps[0]%365+1
    return (année, nb_jours, temps[1], temps[2], temps[3])

import time
def afficheDate(date) :
    if len(date) == 0 :
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    print("jour", date[1], "de l'année", date[0], "à", str(date[2])+":"+str(date[3])+":"+str(date[4]))

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))



def annee_bisextile(annee):
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

def bisextile(jour):
    annee = 1970 
    compteur = 0 
    while jour >= 365 :
        if annee_bisextile(annee) :
            print ("l'année", str(annee), "est bixestile")
            jour -=366
            compteur +=1 
        else :
            jour -=365
        annee += 1
    return compteur
        
bisextile(20000)



def tempsEnDateBisextile(temps):
    jours,heures,minutes,secondes=temps
    jours=jours-bisextile(jours)
    tempsmodifie=(jours,heures,minutes,secondes)
    return tempsEnDate(tempsmodifie)
   
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))



print(secondeEnTemps(int(time.time())))
afficheDate(tempsEnDateBisextile(secondeEnTemps(int(time.time()))))