

def chiffrement(d,fichier):

    """ d : int -> décalage 
                        """
    tab = [] # tableau d'entiers avec tab[0] = nbA , tab[1] = nbB, ...
    nb_lettre = 0 
    for i in range (0,26):
        tab.append(0)
    with open(fichier,"r") as file :
        line = file.readline()
        for k in line :
            nb_lettre+=1
            print(ord(k)+d," ",(ord(k)+d)%65)
            tab[(ord(k)+d)%65]+=1
    file.close()
    print(tab)
chiffrement(4,"test")

