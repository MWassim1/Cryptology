import random

def cryptanalyse(texte,dico_tetragramme):

    file = open(texte,"r")
    line = file.readline()
    tetra = ""
    compteur = 0 
    e = 0 
    while(line):
        for k in line : 
            if(compteur == 4):
                compteur = 0 
                if(tetra in dico_tetragramme): 
                   # print(e," ",dico_tetragramme[tetra]," ",e+int(dico_tetragramme[tetra]))
                    e+=int(dico_tetragramme[tetra])
                else :
                    e+=0.001
                tetra=""

            else : 
                tetra+=k
                compteur+=1
        line = file.readline()
            
    return e 

def chiffrement(texte,alphabet):

    c =""
    with open(texte,"r") as file :
        line = file.readline()
        texte+=line
        for k in line : 
            c+=alphabet[(ord(k)-1)%64]  
    return c



def cryptanalyse_iterative(texte,nb_etape_max):

    dico_tetragramme = {}
    file = open("nb_tetra_fr.csv","r")
    line = file.readline()
    tetra = " "
    freq = " "
    b= 0 # booleen
    while(line):
        for k in line :
            if (b and k=='\n'):
                dico_tetragramme[tetra[1::]] = freq[1::]
            if(b) : 
                freq+=k
            if(k==';'):
                b = 1
            if (not b):
                tetra+=k
            
        freq = " "
        tetra = " "
        b= 0
        line = file.readline()
    file.close()
    e = -10000 # initialise à -infini
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # generation de l'alphabet random :
    alphabet_random = []
    for i in range(26):
        c = random.choice(alphabet)
        while(c in alphabet_random):    
            c = random.choice(alphabet)
        alphabet_random.append(c)
    
    compteur_eg = 0
    i = 0 
    b=0
    while( i < nb_etape_max and compteur_eg != 10):

        texte_chiffre = chiffrement(texte,alphabet_random)
        new_texte = open("new_texte.txt","w")
        new_texte.write(texte_chiffre)
        new_texte.close()
        e_tmp = cryptanalyse("new_texte.txt",dico_tetragramme)
        if (e < e_tmp):
            b =1 
            alphabet = alphabet_random
            e = e_tmp
            r1 = random.choice(alphabet_random)
            r2 = random.choice(alphabet_random)
            while(r1 == r2):
                r2 = random.choice(alphabet_random)
            r_tmp = r1 
            alphabet_random[alphabet_random.index(r1)] = r2
            alphabet_random[alphabet_random.index(r2)] = r_tmp
        else : 
                if(b):
                    b = 0 
                    compteur_eg+=1
                else : 
                    compteur_eg = 0 
                alphabet_random = alphabet
                r1 = random.choice(alphabet_random)
                r2 = random.choice(alphabet_random)
                while(r1 == r2):
                    r2 = random.choice(alphabet_random)
                r_tmp = r1 
                alphabet_random[alphabet_random.index(r1)] = r2
                alphabet_random[alphabet_random.index(r2)] = r_tmp
        i+=1
    print(alphabet,"",i,"",compteur_eg)
    return e 
        
        


def test():
    e= 5
    print(e+int('3'))
    
            
#test()

print(cryptanalyse_iterative("test",1000))
