#1.Sabiranje elemenata liste

sum_list = [1,2,3,4,5,6,7,8,9]

zbir = 0

for i in range (len(sum_list)):
    zbir = zbir + sum_list[i]

print ('Zbir elemenata liste je', zbir)

# ----------------------------------------------------
# Ok boki da krenemo, ovo moze i mnogo lakse da se napise, for petlja moze da prolazi kroz same liste
# ako napises nesto ovako:
#
# for element in sum_list:
#     zbir += element # Ovo je isto skracenica za zbir = zbir + element
#
# ne moras ti da indexiras i prolazis kroz listu, vec for petlja to radi za tebe.
# ------------------------------------------------------
#
# sa druge strane moze i jos lakse. Paython vec dolazi sa ugradjenim funkcijama koje moze da koristis da izracunas nesto u listi
# tipa
#
# sum(list) # sabira sve elemente u listi i vraca resultat
# max(list) # vraca najveci element iz liste
# itd.....
# ---------------------------------------------------------
