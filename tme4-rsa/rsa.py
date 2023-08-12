from math import *

def exp(a, n, p):
    res = 1
    bin_p = bin(n) # récupère la puissance 'n' en base 2 
    for k in bin_p[2::]:
        res = res * res %p
        if(k == '1' ):
            res = res*a % p
    return res

def rsa_chiffrement (x,N,e):
    return exp(x,e,N)

def rsa_dechiffrement (y,p,q,d):
    return exp(y,d,p*q)

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
        return a , v_a , u_a # pgcd(a,b), u , v
    return  a , u_a , v_a

# Retourne s tel que s % n1 == a1 et s % n2 == a2

def crt2 (a1,a2,n1,n2):

    if(a1 > a2):
        c = a2
        M = n2
        p , u ,v = bezout(n1,M)
        c = c * u * n1 + a1 *v * M
        M = M  * n1
        c = c % M
    else : 
        c = a1 
        M = n1
        p , u , v = bezout(n2,M)
        c = c * u * n2 + a2 * v * M
        M = M * n2
        c = c % M


    return c,0

def rsa_dechiffrement_crt (y,p,q,up,uq,dp,dq,N):

    xp = exp(y,dp,p)
    xq = exp(y,dq,q)

    return  (xp*up + xq*uq )%N

#### Wiener
def cfrac(a,b):
    l = []
    k = 0 
    while(b>0):
        l.append(a//b)
        tmp = a
        a = b 
        b = tmp - l[k] * b
        k+=1
    return l

def reduite(L):
   
    if(len(L) == 0):
        return 0,1
    e = L[-1]
    k = 1
    for x in range(-2,-len(L)-1,-1):
        e,k=L[x]*e+k,e
    
    return(e,k)
    

def Wiener(m,c,N,e):
    l = cfrac(e, N)
    l_tmp = []
    for i in range(len(l)+1):
        l_tmp.append(reduite(l[0:i]))
    l = l_tmp
    for (k,d) in l : 
        if(exp(c,d,N)== m):
            return d 
            
    return None


### Generation de premiers
import random
def is_probable_prime(N, nbases=20):
    """
    True if N is a strong pseudoprime for nbases random bases b < N.
    Uses the Miller--Rabin primality test.
    """

    def miller(a, n):
        """
        Returns True if a proves that n is composite, False if n is probably prime in base n
        """

        def decompose(i, k=0):
            """
            decompose(n) returns (s,d) st. n = 2**s * d, d odd
            """
            if i % 2 == 0:
                return decompose(i // 2, k + 1)
            else:
                return (k, i)

        (s, d) = decompose(n - 1)
        x = pow(a, d, n)
        if (x == 1) or (x == n - 1):
            return False
        while s > 1:
            x = pow(x, 2, n)
            if x == n - 1:
                return False
            s -= 1
        return True

    if N == 2:
        return True
    for i in range(nbases):
        import random
        a = random.randint(2, N - 1)
        if miller(a, N):
            return False
    return True


def random_probable_prime(bits):
    """
    Returns a probable prime number with the given number of bits.
    Remarque : on est sur qu'un premier existe par le postulat de Bertrand
    """
    n = 1 << bits
    import random
    p = random.randint(n, 2 * n - 1)
    while (not (is_probable_prime(p))):
        p = random.randint(n, 2 * n - 1)
    return p
