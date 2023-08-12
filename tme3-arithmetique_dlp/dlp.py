from prime import is_probable_prime
import math
import random


#Exercice 1
#Q1
def bezout(a, b):
    """
    a -> int 
    b -> int 

    Retourne le pgcd(a,b) et les coefficients de Bézout u, v tel que u*a + b*v = pgcd(a,b)
                        """
    k = 0 # booleen permettant de savoir si on a échangé les coefficients 
    if(b>a):
        tmp = a 
        a = b  
        b = tmp
        k =1

    u_a = 1 
    u_b = 0
    v_a = 0 
    v_b = 1


    while(b> 0 ):
        q = a//b

        b_new  = a- q*b
        a = b
        b = b_new 

        u_new = u_a - q*(u_b)
        u_a = u_b
        u_b = u_new

        v_new = v_a - q*(v_b)
        v_a = v_b
        v_b = v_new

    if(k):
        return a , v_a , u_a
    return  a , u_a , v_a


#Q2
def inv_mod(a, n):

    """
        a -> int 
        n -> int 

        Retourne l'inverse modulaire de a 
            """
    
    for i in range(n):
        if( (a*i)%n == 1):
            return i
    return -1


def invertibles(N):
    L = []
    for k in range(N) : 
        if(inv_mod(k,N)!= -1 ):
            L.append(k)
    return L


#Q3
def phi(N):
    e = 0 
    for i in range (1,N):
        pgcd,u,v = bezout(i,N)
        if(pgcd == 1  ): # donc ils sont premiers entre eux
            e+=1

    return e


#Exercice 2
#Q1
def exp(a, n, p):
    res = 1
    bin_p = bin(n) # récupère la puissance 'n' en base 2 
    for k in bin_p[2::]:
        res = res * res %p
        if(k == '1' ):
            res = res*a % p
    return res



#Q2
def nb_prem():
    res = []
    est_prem = 1
    for i in range(2,1000):
        for j in range(2,i):
            if( (i%j) == 0 ):
                est_prem = 0 
                break
        if(est_prem == 1):
            res.append(i)
        est_prem = 1
    return res

def factor(n):
    res = []
    p = 0
    index = 0 
    liste_nb_prem = nb_prem() # on récupère une liste de nombres premiers
    while(n>1):
        if(n%liste_nb_prem[index] == 0 ): # on regarde si le nombre premier divise 'n'
            p+=1 # alors on incrémente de 1 la puissance du nombre premier 
            n = n//liste_nb_prem[index]
        elif(p != 0):
            res.append((liste_nb_prem[index],p))
            p = 0
            index+=1
        else :
            p = 0 
            index+=1
    res.append((liste_nb_prem[index],p))
    return res


#Q3
def order(a, p, factors_p_minus1):
    res = 1
    factor_order = []
    l_tmp = []
    factor_a = factor(a)

    # Dans ce bloc de code on va decomposer nos entiers en produit de facteur premier dans l'ordre croissant   puis récuperer dans 'factor_order' la décomposition de 'a' en complétant avec les facteurs manquants de la décompision de 'p-1'
    for x in factor_a : 
        l_tmp.append(x[0])
    for x in range(len(factors_p_minus1)):
        if( factors_p_minus1[x][0] not in l_tmp):
            factor_order.append(factors_p_minus1[x])
        else : 
            factor_order.append((factors_p_minus1[x][0],factors_p_minus1[x][1]-factor_a[x][1]))

    
    for x in factor_order: # on récupère le plus petit 'k'
        res *=x[0]**x[1]
        if(exp(a,res,p) == 1):
            break
    return res


#Q4
def find_generator(p, factors_p_minus1):

    return order(2,p,factors_p_minus1)


#Q5
def generate_safe_prime(k):
    q= random.randint(0,1000)
    while(is_probable_prime(q,k)== False or is_probable_prime(2*q+1,k) == False ): 
        q= random.randint(0,1000)
    return 2*q+1


#Q6

def bsgs(n, g, p):
    # log(n)_g ** p --> g^x = n[p]
    s = math.ceil(math.sqrt(p-1))

    # on construit un dictionnaire "pas de bébé"
    dico_baby_step = {}

    for k in range(s):  
        dico_baby_step[exp(g,k,p)]=k
   # print(dico_baby_step)
    y = exp(g, s*(p-2), p)

    # "pas de géant"
    for j in range(s):
        tmp= (n*exp(y, j, p)) % p
        if tmp in dico_baby_step:
            return j*s + dico_baby_step[tmp]
    print("Erreur aucun resultat trouvé !")
    return -1