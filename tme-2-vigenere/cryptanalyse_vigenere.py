# Sorbonne Université 3I024 2021-2022
# TME 2 : Cryptanalyse du chiffre de Vigenere
#
# Etudiant.e 1 : MUSSARD WASSIM - 28706762
# Etudiant.e 2 : NOM ET NUMERO D'ETUDIANT

import sys, getopt, string, math

# Alphabet français
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Fréquence moyenne des lettres en français
# À modifier
freq_FR = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

def frequence(fichier):
    """
        fichier : str -> nom du fichier

        MEt à jour freq_FR
            """
    global freq_FR
    nb_lettre = 0 
    with open(fichier,"r") as file :
        line = file.readline()
        for k in line :
            nb_lettre+=1
            freq_FR[(ord(k)-1)%64]+=1
    file.close()
    for k in range(0,26) : 
        #print(chr(l),tab[k]/nb_lettre)
        freq_FR[k] = freq_FR[k]/nb_lettre


# Chiffrement César
def chiffre_cesar(txt, key):

    """ key : int -> décalage 
        txt : str -> chaine de caractères (message clair)

        HYPOTHESE : txt est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

        Retourne le texte ayant été chiffré par la méthode de césar 
                        """
    c = ""
    for k in txt :
        tmp = ord(k)+key # on applique notre décalage "key"
        if(tmp > 90): # si on dépasse 90 ( 'Z' ) alors on doit retourner au début de notre alphabet 
            c+=chr(((ord(k)+key)%90)+64) # pour cela , on utilise l'opération du "%" , et on ajoute 64 pour retourner un caractère appartenant à notre intervalle 
        else :
            c+=chr(tmp) # sinon aucun problème , donc on ajoute notre caractère
    txt = c 
    return txt

# Déchiffrement César
def dechiffre_cesar(txt, key):

    """
        key : int -> décalage 
        txt : str -> chaine de caractères (message chiffré) 

        HYPOTHESE : txt est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

        Retourne un texte déchiffré qui a été chiffré par la méthode de césar 
                        """
    dec = ""
    for k in txt:
        tmp = ord(k) - key # on fait l'opération inverse, en retirant notre décalage "key"
        if (tmp >= 65): # on regarde si le resultat est supérieur ou égal à 65, si c'est la cas alors pas de problème , c'est à dire qu'on n'a pas fait de "modulo" pour le chiffrement 
            dec+=chr(tmp)
        else :
            dec += chr(90+(tmp-64)) # sinon on a probablement fait un modulo lors du chffirement , donc on doit retirer 64 et retirer à 90 le resultat obtenu pour obtenir un caractère appartenant à notre intervalle 
    txt = dec 
    return txt

# Chiffrement Vigenere
def chiffre_vigenere(txt, key):

    """
        txt : str -> chaine de caractères (message clair)
        key : str -> chaines de caractères (clé permettant le chiffrement du message )

        HYPOTHESE : txt est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces 

        Retourne le texte chiffré par la méthode de Vigenère 
                    """
    
    c =""
    i_key = 0 # indice/index nous indiquant la lettre en cours a affecté au 'txt'
    for k in  txt :
        if(i_key == len(key)): # on  reset l'indice à 0 
            i_key = 0
        tmp = ord(k)+key[i_key]
        if(tmp > 90): # si on dépasse 90 ( 'Z' ) alors on doit retourner au début de notre alphabet 
            c+=chr(((ord(k)+key[i_key])%90)+64) # pour cela , on utilise l'opération du "%" , et on ajoute 64 pour retourner un caractère appartenant à notre intervalle 
        else :
            c+=chr(tmp) # sinon aucun problème , donc on ajoute notre caractère
        i_key+=1
    txt=c
    return txt

# Déchiffrement Vigenere
def dechiffre_vigenere(txt, key):
    
    """
        txt : str -> chaine de caractères (message clair)
        key : str -> chaines de caractères (clé permettant le déchiffrement du message )

        HYPOTHESE : txt est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

        Retourne le texte déchiffré qui a été chiffré par la méthode de Vigenère
                    """
    dec = ""
    i_key = 0 
    for k in txt:
        if(i_key == len(key)): # on  reset l'indice à 0 
            i_key = 0
        tmp = ord(k) - key[i_key] # on fait l'opération inverse, en retirant notre décalage "key"
        if (tmp >= 65): # on regarde si le resultat est supérieur ou égal à 65, si c'est la cas alors pas de problème , c'est à dire qu'on n'a pas fait de "modulo" pour le chiffrement 
            dec+=chr(tmp)
        else :
            dec += chr(90+(tmp-64)) # sinon on a probablement fait un modulo lors du chffirement , donc on doit retirer 64 et retirer à 90 le resultat obtenu pour obtenir un caractère appartenant à notre intervalle
        i_key+=1
    txt = dec 
    return txt

# Analyse de fréquences
def freq(txt):
    """
        txt : str -> chaine de caractères

        HYPOTHESE : txt est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

        Retourne un tableau de fréquence des lettres de 'txt'
                    """

    hist=[0.0]*len(alphabet)# tableau d'entiers avec hist[0] = nbA , hist[1] = nbB, ...
    nb_lettre = 0
    for k in txt:
        nb_lettre+=1
        hist[(ord(k)-1)%64]+=1
    return hist

# Renvoie l'indice dans l'alphabet
# de la lettre la plus fréquente d'un texte
def lettre_freq_max(txt):
    """
        txt : str -> chaine de caractères

        HYPOTHESE : txt est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

        Retourne l'indice de la lettre la plus présente dans 'txt'
                """

    hist = freq(txt)
    i_max = 0
    for k in range(1,len(hist)):
        if( hist[k] > hist[i_max]):
            i_max = k
    return i_max

# indice de coïncidence
def indice_coincidence(hist):

    """
        hist : int[] -> tableau de fréquence d'un texte 

        HYPOTHESE : _____________

        Retourne l'indice de coïncidence de notre tableau
                """
    
    i_coincidence = 0.0
    nb_lettre = 0
    for k in hist : # on compte le nombre de lettres dans notre histogramme
        nb_lettre+=k
    for n in hist :
        if((nb_lettre*(nb_lettre-1)) == 0):
            return i_coincidence
        i_coincidence+=(n*(n-1))/(nb_lettre*(nb_lettre-1)) # on applique la formule 
    return i_coincidence

# Recherche la longueur de la clé
def longueur_clef(cipher):
    """
        cipher : str -> chaines de caractères 

        HYPOTHESE : cipher est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

        Retourne la longueur de la clé selon l'indice de coïncidence
                """

    key_length = 3 # variable permettant de connaître la longueur de la clé 
    m_ic = 0 # moyenne de l'indice de coïncidence 
    while (m_ic <= 0.06 and key_length <= 20 ):
        ic = 0 # indice de coïncidence 
        nb_iterations =  0
        d = 0 # debut du bloc 
        f = key_length # fin du bloc  
        for d in  range(key_length):
            hist=freq(cipher[d:len(cipher):key_length])  #pour pouvoir calculé l'indice de coïncidence, on récupère l'histogramme associé au texte passé en argument 
            ic += indice_coincidence(hist)
            d = f
            f = d + key_length
            nb_iterations+=1
        m_ic = ic/nb_iterations
        key_length+=1
    return key_length-1




    return 0
    
# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en utilisant la lettre la plus fréquente
# de chaque colonne
def clef_par_decalages(cipher, key_length):
    """
    cipher : str -> chaines de caractères
    key_length : int -> longueur de la clé 

    HYPOTHESE : cipher est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces 

    Retourne un tableau représentant la clé décalée 


    """
    decalages=[0]*key_length
    e = ord('E') # on commence par récupérer ord('E') qui va nous permeetre de calculer le décalage du cractère le plus fréquent .
    for k in range(key_length): # on parcourt notre 'cipher' jusqu'à key_length car il est multiple de la  taille du texte .
        decalages[k] =  (lettre_freq_max(cipher[k:len(cipher):key_length]) - (e-65))%26 # on filtre 'cipher' sur la colonne du texte qui nous interesse par pas key_length 
                                                                                        #( et on fait  '- 65' pour avoir un entier  qui appartient à notre intervalle d'étude)    
    return decalages

# Cryptanalyse V1 avec décalages par frequence max
def cryptanalyse_v1(cipher):
    """
    cipher : str -> chaine de caractères 
    
    HYPOTHESE : cipher est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

    Retourne le texte chiffré passé en paramètre en un texte clair respectif   
    """
    decalages =clef_par_decalages(cipher,longueur_clef(cipher)) # on récupère le tableau de decalage à l'aide de la longueur de la clef .

    # A présent dechiffrons 'cipher' à l'aide du tableau de décalage et la fonction dechiffre_vigenere 

    return  dechiffre_vigenere(cipher,decalages)
"""

REPONSE A LA QUESTION : Nous nous retrouvons avec 18 textes correctement cryptanalysés. On pourrait expliquer ce résultat par le fait qu'on peut avoit une source d'erreur avec  
l'hypothèse sur la lettre la plus fréquente dans une colonne de taille 'key_length' et qui est la lettre 'E'. Or ca ne doit pas être une véritée générale,
il y a probablement des textes où le 'E' n'est pas la lettre la plus fréquente.

"""

################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V2.

# Indice de coincidence mutuelle avec décalage
def indice_coincidence_mutuelle(h1,h2,d):
    """
    h1 : int[] -> tableau d'entiers représentant la fréquence d'un texte / colonne 
    h2 : int[] -> tableau d'entiers représentant la fréquence d'un texte / colonne 
    d : int -> décalage

    Retourne l'indice de coïncidence mutuelle entre h1 et h2 (où h2 a subi un décalage de 'd')

    """
    icm = 0
    nb_lettreh1 = 0 
    nb_lettreh2 = 0 
    tab_tmp=[0]*len(h1)
    
    for k in range(26):
        tab_tmp[k] = h1[k]*h2[(k+d)%26]
        nb_lettreh1+=h1[k]
        nb_lettreh2+=h2[k]
    for k in range(26):
        icm+=tab_tmp[k]/(nb_lettreh1*nb_lettreh2)
    return icm

# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en comparant l'indice de décalage mutuel par rapport
# à la première colonne
def tableau_decalages_ICM(cipher, key_length):
    """
    cipher : str -> chaine de caractères 
    key_length : int -> taille de la clé 

    HYPOTHESE : cipher est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

    Retourne un tableau d'entiers représentant les décalages qui maximise les indices de coïncidence mutuelle 
    """
    decalages=[0]*key_length
    colonne = cipher[0:len(cipher):key_length] # récupère la première colonne 
    for k in range(key_length):
        icm = 0
        index =  0
        tmp_colonne = cipher[k:len(cipher):key_length] # on récupère la colonne k 
        for j in range(26): # on boucle jusqu'à 26 (car on a 26 lettres, on va tester les 26 décalges possible ) pour trouver l'icm max entre les 26 itérations 
            tmp_icm = indice_coincidence_mutuelle(freq(colonne),freq(tmp_colonne),j) # on calcule l'indice de coïncidence entre la première colonne et la colonne k avec un décalage 'j'.
            if(icm < tmp_icm): 
                icm = tmp_icm
                index = j # on récupère l'indice qui donne l'icm max (l'indice j ==> lettre j )
        decalages[k] = index

        
    return decalages

# Cryptanalyse V2 avec décalages par ICM
def cryptanalyse_v2(cipher):
    """
    cipher : str -> chaine des caractères 

    HYPOTHESE : cipher est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

    Retourne 'cipher' déchiffré 
    """
    # On suit les étapes données dans l'énoncé 
    key_length = longueur_clef(cipher)  # on récupère la longueur de la clé 
    decalages = tableau_decalages_ICM(cipher,key_length) # le tableau de décalage 
    t_vigenere = dechiffre_vigenere(cipher,decalages) #déchiffre à l'aide de vegenère 
    t_cesar = dechiffre_cesar(t_vigenere,(lettre_freq_max(t_vigenere)-4)%26) # puis comme un texte chiffré avec cesar . 
    return t_cesar
"""
REPONSE A LA QUESTION : Nous observons que 45 textes sur 100 on été cryptanalysés. Ce qui est beaucoup mieux que cryptanalyse_v1 . 
On pourrait supposer qu'ici nous utilisons une approche moins aléatoire ce qui augmente l'efficacité de notre algorithme. 
En effet , ici on ne suppose pas que la lettre 'E' est la lettre la plus représentée . Donc on évite de potentiels erreurs .

"""
################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V3.

# Prend deux listes de même taille et
# calcule la correlation lineaire de Pearson
def correlation(L1,L2):
    """
    L1 : int[] -> tableau d'entiers 
    L2 : int[] -> tableau d'entiers

    HYPOTHESE : L1 et L2 doivent être de même taille 

    Retourne la corrélation entre L1 et L2  
    """
    esp1 = 0 
    esp2 = 0 
    numerateur = 0.0
    denominateur_x= 0.0
    denominateur_y = 0.0

    #Calcul des espérences de L1 et L2 
    for i in range(len(L1)):  # len(L1) == len(L2)
        esp1+=L1[i]
        esp2+=L2[i]
    esp1 = esp1/len(L1)
    esp2 = esp2/len(L2)

    #Calcul de la corrélation 
    for i in range(len(L1)):
        numerateur+= (L1[i]-esp1)*(L2[i]-esp2)
        denominateur_x+= (L1[i]-esp1)**2
        denominateur_y+= (L2[i]-esp2)**2
    return round(numerateur/(math.sqrt(denominateur_x) * math.sqrt(denominateur_y)),7) # on arrondit (arbitrairement) le resultat à 7 chiffres après la virgule 

# Renvoie la meilleur clé possible par correlation
# étant donné une longueur de clé fixée
def clef_correlations(cipher, key_length):
    """
    cipher : str -> chaines de caractères 
    key_length : int -> taille de la clé 

    HYPOTHESE : cipher est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

    Retourne un tuple (x,y) où 'x' représente la moyenne des correlation max et 'y' est un tableau d'entiers contenant les décalages des correlation max . 
    
    """
    key=[0]*key_length
    score = 0.0
    corr_moy = 0
    frequence("./germinal_nettoye") #met à jour freq_FR
    for k in range(key_length):
        corr_max = -10000 # initialise à -infini
        for dec in range (26): # teste les 26 décalges possible
            tmp_chiffre = chiffre_cesar(cipher,dec) # on chiffre le texte avec une 'clé' = 'dec' afin de voir si ce décalage nous donne une correlation max  
            tmp_corr= correlation(freq_FR,freq(tmp_chiffre[k:len(cipher):key_length])) # on applique la primitive correlation avec freq_FR ( comme suggéré dans l'énoncé ) avec le texte chiffré découpé en colonne de taille 'key_length'
            if(corr_max < tmp_corr):
                corr_max = tmp_corr
                e = (26-dec)%26 # récupère le décalage qui maximise la correlation 
        corr_moy+=corr_max
        key[k] = e
    score = corr_moy/key_length
    return (score, key)

# Cryptanalyse V3 avec correlations
def cryptanalyse_v3(cipher):
    """
    cipher : str -> chaines de caractères 

    HYPOTHESE : cipher est une chaine de caractères dont tous les caractères appartient  à notre alphabet , sans ponctuations , ni espaces

    Retourne 'cipher' sous son message clair 
    """
    c_max = -100000 # initialise à -infini
    for key_length in range(1,21): # taille de clé allant de 1 à 21 exclu 
        c = clef_correlations(cipher,key_length) # pour chaque taille de clé (key_length), on récupère la correlation max 
        if(c[0]> c_max): # test pour savoir si la nouvelle moyenne de correlation est meilleure que 'c_max'
            c_max = c[0]
            key_lengthMAX = c[1] # on récupère la taille de clé associée au 'c_max'
    cipher_dechiffre = dechiffre_vigenere(cipher,key_lengthMAX) # enfin on applique comme indiqué dans l'énoncé un dechiffrement de vigenere avec la clé max sur le texte .

    return cipher_dechiffre
"""

REPONSE A LA QUESTION : Ici, on obtient 94 textes correctement cryptanalysés . 
Les 6 textes qui échouent le test partagent les caractéristiques suivantes : longueur
        -> la taille de la clé n'est pas de longueur multiple de la longueur du texte . 
        -> la correlation max est pas assez proche de 1. On remarque que ces textes ne dépasse pas 0.7. Nous ne disons pas qu'avoir une correlation max c < 0.7 nous donnera un résultat faux.
            Mais il est possible que ce dernier facteur puisse provoque un résultat non attendu.

La méthode utilisée est beaucoup plus efficace que les 2 autres cryptanalyse . En effet car ici , nous utilisons la correlation entre histogramme de fréquence.
Donc plus on est proche de 1 plus le texte qu'on essaye de déchiffré  est proche du francais, et donc limite fortement les sources d'erreurs. Or, on a pu constater que certains textes sont passés 
à travers de notre de cryptanalyse . Ces derniers peuvent être soumis à plusieurs sources d'erreurs tel que la longueur de la clé qui n'est pas multiple de la longueur du texte. Ou encore 
une correlation max pas assez précise, pas assez proche de 1. 

"""

################################################################
# NE PAS MODIFIER LES FONCTIONS SUIVANTES
# ELLES SONT UTILES POUR LES TEST D'EVALUATION
################################################################


# Lit un fichier et renvoie la chaine de caracteres
def read(fichier):
    f=open(fichier,"r")
    txt=(f.readlines())[0].rstrip('\n')
    f.close()
    return txt

# Execute la fonction cryptanalyse_vN où N est la version
def cryptanalyse(fichier, version):
    cipher = read(fichier)
    if version == 1:
        return cryptanalyse_v1(cipher)
    elif version == 2:
        return cryptanalyse_v2(cipher)
    elif version == 3:
        return cryptanalyse_v3(cipher)

def usage():
    print ("Usage: python3 cryptanalyse_vigenere.py -v <1,2,3> -f <FichierACryptanalyser>", file=sys.stderr)
    sys.exit(1)

def main(argv):
    size = -1
    version = 0
    fichier = ''
    try:
        opts, args = getopt.getopt(argv,"hv:f:")
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-v"):
            version = int(arg)
        elif opt in ("-f"):
            fichier = arg
    if fichier=='':
        usage()
    if not(version==1 or version==2 or version==3):
        usage()

    print("Cryptanalyse version "+str(version)+" du fichier "+fichier+" :")
    print(cryptanalyse(fichier, version))
    
if __name__ == "__main__":
   main(sys.argv[1:])
