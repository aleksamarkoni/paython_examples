# 11. Напишите Питхон функцију која узима две листе и враћа Труе ако имају бар
# једног заједничког члана.

lista_1=[]
lista_2=[]

L1=int(input('Broj clanova i clanovi prve liste'))
for i in range(L1):
    j=input()
    lista_1.append(j)

L2=int(input('Broj clanova i clanovi druge liste'))
for i in range(L2):
    k=input()
    lista_2.append(k)

for i in lista_1:
    for j in lista_2:
        if i==j:
            print ('True')

# -------------------------------------------
# Ovo je bas zanimljiv zadatak, to be honest, ali ovo tvoje resenje ce da istampa True mnogo puta, ako liste imaju vise
# zajednickih elementa, u ovom tvom slucaju, fora je da prekines ako naidjes na takav element. E sada treba da vidis kako
# ovde da prekines i nastavis dalje, sto uopste nije lako jer se nalazis ne unutar jedne, nego unutar druge for petlje,
# takozvane ugnjezdene for petlje :) Ovo cu zapisati kao pitanje za sledeci cas, jer je dosta bitno.
# --------------------------------------------
# Drugi problem je kako ovo optimizovati, jer ti sada ovde prolazis za svaki element prve liste kroz drugu listu.
# sto znaci da ako imas neke liste duzine N i M, onda ti imas N x M operacija.
# Postoji specijalna notacija koja objasnjava koliko nesto traje, O notacija, o kojoj cemo pricati, zapisao u pitanja, ali ukratko
# O(1) - jedna instrukcija
# O(N) - n instrukcija, kao tipa kada prolazis kroz niz koji ima N elemenata
# O(Nˆ2) - n x n instrukcija, tvoj slucaj ovde, kada n puta prolazis kroz niz koji ima n elemenata
# O(NˆN) - ludilo :)
#
# sto je ovaj izraz u zagradama kod O() kompleksniji, onda je algoritam slozeniji.
#
# Ovo se koristi da objasni koliko je algoritam efikasan i super je fora. Pricacemo o tome.
#
# Da se vratimo na ovo ovde, da li sada mozda mozes bolje i brze ovde da vidis sta se desava.
#
# Mozda da nekako iskoristis setove.
# za vise informacija moramo otici na ovaj link
# https://stackoverflow.com/questions/3170055/test-if-lists-share-any-items-in-python
# tu imas dobro objasnjeno razlicite methode i koja je najbolja, ali nemoj da se smoris, ovo je ono kada se bas udubis
# ja cu ti ovo sve objasniti, da ti stoji negde u malom mozgu, pa cemo taj dokument otvoriti opet za jedno godinu dve,
# # da vidis da li ima napretka :)
# # -------------------------------------------------
# naravo mogao si i in operator da koristis,
# ako zelis da proveris da li nesto postoji u nizu ili ne, mozes jednostavno da uradis if element in lista i on ti kaze true false.
# ---------------------------------------------------

