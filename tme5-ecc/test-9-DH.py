from ecc import *

print("\n\n----------------------------------------------\n\n")

# print(point_aleatoire_naif((360040014289779780338359, 117235701958358085919867, 18575864837248358617992)))

# print(point_aleatoire((360040014289779780338359, 117235701958358085919867, 18575864837248358617992)))



print("Test 9 : Echange de clé DH")

print("---------------------")

print("Test DH")
p = 1558360324771
n = 389590081193
E = (p,1,0) ##   #E = 4 n et n est un nombre premier
N_factors = ( (2,2),(n,1) )
N = 4*n
P = point_ordre(E,N,N_factors,n)
# print("P : ",P,ordre(N,N_factors, P, E),N)
assert point_sur_courbe(P,E)
assert n == ordre(N,N_factors,P,E)
(sA,PA) = keygen_DH(P,E,n);
(sB,PB) = keygen_DH(P,E,n);
# print((sA,PA),(sB,PB))
assert est_egal(echange_DH(sA,PB,E), echange_DH(sB,PA,E),p)


print("Test DH : OK")

print("\n\n----------------------------------------------\n\n")
p = 248301763022729027652019747568375012323
N = 248301763022729027652019747568375012324
factors_N = [(2, 2), (62075440755682256913004936892093753081, 1)]
E = (p, 1, 0)
assert bon_point(p,N,factors_N,E)