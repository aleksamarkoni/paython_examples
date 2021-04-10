# 19. Напишите Питхон програм да бисте добили разлику између две листе.

lista_1 = [1,2,3,4,5,6,7,8,9]
lista_2 = [4,5,6,7,8,9,10,11,12]
l=[]
for i in range (len(lista_1)):
    if not lista_1[i] in lista_2:
        l.append(lista_1[i])

for j in range (len(lista_2)):
    if not lista_2[j] in lista_1:
        l.append(lista_2[j])

print ('Razlika listi',lista_1,'i',lista_2,'je',set(l))                


# -------------------------------------
# Ovo je ok, ali pitaanje je da li moze brze, recimo koristeci setove
# -------------------------------------
# Krajnje je vreme da pocnes da ucis kako mozes generisati novu listu
# pazi ovo parce coda
#
# prva_lista = [for e in lista_1 if e not in lista_2] # opet ovaj in operator
#
# ovo je bas mocna fora, takozvani inicijalizatori listi, u ovom konkretnom primeru je mozda malo teze, ali pazi ovo
#
# zamisli treba ti lista neparnih brojeva do 20, mozes da kazes nesto ovako
#
# lista = [for i in range(1, 20, 2)]
#
# sta se ovde desilo, koristis for petlju unutar []
# sta to znaci pythonu, pa on ce da uzme rezultat od ovog fora, to jest svaki i ce da upise u listu, kao da si je sam appendovao.
# Mozes tako da shvatis, da ne bi pisao append stalno.
#
# ajde da se vratimo na gornji primer, i slobodno ga uporedi sa onim tvojim gore, sve je isto osim sto ja koristim in, i nema append
# koji zbog ove sintakse ne treba, tako da
#
# prva_lista = [for e in lista_1 if e not in lista_2] # opet ovaj in operator
#
# znaci napravi mi jednu novu listu, od svih elemenata iz liste_1 koji nisu u lista_2, i ovo je bas citljivo kao da nisi pisao code.
# Covek kada cita ovo, i neko mozda ko se prvi put susretne sa forom videce sta se u stvari radi.
#
# e sada kako resiti zadatak, pa vrlo prosto
#
# prvi_koji_nisu_u_drugoj = [for e in lista_1 if e not in lista_2]
# drugi_koji_nisu_prvoj = [for e in lista_2 if e not in lista_1]
# rez = prvi_koji_nisu_u_drugoj + drugi_koji_nisu_prvoj
#
# ako uradis + nad listama, on bukvalno napravi novu listu tako sto nadoveze drugu na prvu.
# Obrati isto paznju da ti ovde ne treba da od rez liste pravis set, posto je nemoguce da se pojave dva ista elementa u ove dve liste
# Pitanje je zasto !!!, Razmisli malo o tome.
# --------------------------------------------------------------