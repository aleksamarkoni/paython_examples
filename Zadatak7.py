#Напишите Питхон програм за уклањање дупликата са листе.

L=[1,2,3,4,5,6,7,8,9,10,2,4,6,8,10]
d=[]

duplikati = set()

for x in L:
    if x not in duplikati:
        d.append(x)
        duplikati.add(x)

print(d)

# ---------------------------------------
# ok ovo je ok, zato sto si koristio set, ima i malo bolja fora,
#
# ako napises set(L) on ce od te L liste napraviti set, a moze i kontra, ako imas set S a treba ti lista onda uradis list(S)
#
# tako da ovo moze da se skrati ovako
# L = [1, 2, 3, ....]
# S = set(L) # prilikom pravljenja seta, on ce da izbaci duplikate
# bez_duplikata = list(S) # a ovde samo vratis set u listu
# print(bez_duplikata)
#
# a moze i jos krace, da ne bi uvodio ove pomocne promenljive
# L = [1, 2, 3, .......]
# print(list(set(L)))
#
# ------------------------------------------------------
# E sada ja bi ipak voleo da se malo vratis unazad, u ono tvoje godina proizvodnje, i da probas da ovaj zadatak resis bez seta,
# vec da uradis nesto ovako
# da umesto if x not in duplikati, napravis funkciju, koja uzima listu i element, i onda vraca true ili false,
# u zavisnosti da li se element nalazi u listi ili ne.
#
# evo ja cu napraviti definiciju a ti popuni ostalo
#
# fun da_li_se_element_nalazi_u_listi(lista, element):
#     #ovde treba da dodje kod koji proverava da li se u lista nalazi element
#     #ovde vratis resultat
#
# kada napravis tu funkciju, probaj da zamenis gornji program, tako da koristi tu sada funkciju, umesto ovog gore, i onda mozes da izbacis set.
#
# Kada to napravis, imam jos jedan zadatak za tebe, a to je da vidis sta radi operator in nad listom i sta se desi kada napises nesto ovako
# if element in lista:
#     #ovde dodje neki code
# ovo sa setom je resenje koje ce najbrze raditi, ali ok, pitanje je pravo, koje je resenje brze, optimalnije i sta su razlike
# ali o tome cemo malo kasnije diskutovati.
# ------------------------------------------
#
