def frequence(fichier):
    tab = [] # tableau d'entiers avec tab[0] = nbA , tab[1] = nbB, ...
    nb_lettre = 0 
    for i in range (0,26):
        tab.append(0)
    with open(fichier,"r") as file :
        line = file.readline()
        for k in line :
            nb_lettre+=1
            tab[(ord(k)-1)%64]+=1
    file.close()
   # print("\n",tab,"\n")
    l = 65 
    for k in range(0,26) : 
        #tab[k] = round(tab[k]/nb_lettre,2)
        print(chr(l),tab[k]/nb_lettre)
        l+=1
    return tab 


frequence("test")

    
    
    

    