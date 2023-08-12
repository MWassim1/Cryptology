from frequence import *


texte = ""

def mono_alphabetique_chiffrement(fichier_alphabet,fichier):
    global texte 
    """
        fichier_alphabet : str -> indique le nom du fichier contenant l'alphabet associé au chiffrement , qui doit respecter le format suivant  : AZDVHFESCV... ( pas d'espaces,virgules,saut de lignes...ET  alphabet[0] <-> A , alphabet[1] <-> B ... // par ex ici alphabet[1] = Z <-> B)
        fichier : str -> indique le nom du fichier à chiffré """
    texte = ""
    file = open(fichier_alphabet,"r")
    alphabet = file.readline()
    file.close()
    c = ""
    with open(fichier,"r") as file :
        line = file.readline()
        texte+=line
        for k in line : 
            c+=alphabet[(ord(k)-1)%64]  # on accede à notre alphabet pour pouvoir y récuperer le caractère associé à la position (ord(k)-1)%64
    return c

def mono_alphabetique_dechiffrement(fichier_alphabet,s):
    global texte
    """
        s : str -> chaine chiffré avec un chiffrement mono alphabétique
                    """
    file = open(fichier_alphabet,"r")
    alphabet = file.readline()
    file.close()
    dec = ""
    index = 0 
    for k in s :  
        for e in alphabet : # on parcourt notre alphabet à la recherche du caractère 'k' 
            if (e==k):
                dec+=chr(index+65)
                index = 0
                break
            index+=1
    if (dec == texte):
        print("Déchiffrement réussi ! ")
    else : 
        print("Déchiffrement raté !")
    return dec

def ecrire_file(s,b):
    """
        s : str -> chaine codée ou non
        b : boolean -> 1 : codé
                       0 : non codé ( <--> déchiffré) """
    if(b) :
        file = open("texte_chiffre.txt","w")
        f = "texte_chiffre.txt"
    else :
        file = open("texte_nonchiffre.txt","w")
        f = "texte_nonchiffre.txt"
    file.write(s)
    file.close()
    frequence(f)

            
print(mono_alphabetique_dechiffrement("code_mono_alphabetique",mono_alphabetique_chiffrement("code_mono_alphabetique","test")))
ecrire_file(mono_alphabetique_chiffrement("code_mono_alphabetique","test"),1)
ecrire_file(mono_alphabetique_dechiffrement("code_mono_alphabetique",mono_alphabetique_chiffrement("code_mono_alphabetique","test")),0)

""" En comparant les histogrammes des fréquences clair et du chiffré on retrouve aussi "une relation logique" entre ces histogrammes. 
    Par exemple avec le code mono-alphabetique : AZERTYUIOPQSDFGHJKLMWXCVBN , on obtient un texte chiffré avec peu de 'C', avec une fréquence x. 
    En déchiffrant ce texte , on a alors une fréquence de 'X' qui aura une fréquence de x aussi. 
 """