# 14. Напишите Питхон програм за штампање бројева одређене листе након уклањања
# парних бројева са ње.

Lista = [1,2,3,4,5,6,7,8,9,10]

for i in Lista:
    if 1//2 == 0:
        Lista.remove(i+1)

print (Lista)


# ------------------------------------
# he he, kako super primer, ovo ce da radi, zato sto je python super jezik i njegoa remove i for petlja nece da se zaglupe :)
#
# ali ovo je super primer, i o ovome moramo da pricamo.
#
# recimo da nemas ovu remove funkciju, nego da moras da samo uklanjas element iz liste, ili jos prostije, kako bi napisao program
# da uneti element ukloni iz liste (pretpostavimo da ga ima u listi), ali da ne znas za ovu funkciju nego da moras da je
# napises od nule sto bi rekli.
#
# Ima vise nacina da se to uradi.
#
# Mislim najednostavni nacin je da recimo napravis novu listu, i da tamo prebacis sve elemente osim tih koji ti ne trebaju.
# Tipa napravis novu listu, i appendujes sve elemente koji su neparni na nju. Posle toga proglasis tu novu listu, da ti je ta stara
# to jest kopiras novu u staru i to je to.
#
# E sada kod ovog nacina sa novom listom imas problem sto trosis memoriju, jer pravis dve liste.
#
# Postvlja se pitanje da li mozes da modifikujes postojecu listu, bez pravljenja nove, tako da uklonis taj element iz nje.
# To se zove takozvani in place method, jer radis sve u mestu, to jest u samoj listi.
#
# E sada, hmm, ovde je pitanje, sta tacno gledamo i kako, da li je to niz ili lista (velika i vazna tema), ali ajde da
# kazemo da je to niz, i da je svaki element u memoriji jedan pored drugog.
# recimo imas 100 elemenata koji stoje jedan pored drugog, i onda ti kada kazes niz[50], znas sta treba da radis, jer nemas rupa
# jednostavno ides redom i brojis mesta, kada dodjes do 50og mesta onda je to to. E sada kako ukloniti 50 element, jer ako ga samo ponistis
# pojavljuje se rupa na toj 50 pozicij, tako da kao da si prekinuo niz na dva dela,
# i onda se sam koncept niza zezne, jer nisu svi elementi u njemu jedan pored drugog. Zbog toga, da bi niz ostao
# konzistentan, moras sve elemente posle uklanjanja 50og da pomeris ulevo za jedan, tako da ti 51 dolazi na 50 mesto,
# 52 na 51 .... poslednji na pretposlednje i onda ti ta rupa bukvalno bude na kraju, ali ti kazes, ok, sve je super, niz
# ima jedan element manje, pa ona rupa na kraju, samo cu reci nema 100 nego 99 mesta, tako da neces ni stici do te
# rupe na kraju. Mislim ovo je velika tema i moramo o njoj pricati, zasto sada ovaj tvoj algoritam radi i sta radi ovaj for
# i sta radi ova funkcija remove, ali uopste nije tako jednostavno.
# ----------------------------------------------------------------------
