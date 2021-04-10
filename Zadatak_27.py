# 27. Напишите програм за Питхон да бисте пронашли други најмањи број на листи.

lista=[1,1,2,2,3,4,5,5,6,8,9,7,9,10,10]
lista.sort()

i=len(lista)-1
j=0

while j<i:
    if lista[j] < lista[j+1]:
        print ('Drugi najmanji broj u listi',lista,'je',lista[j+1])
        break
    else:
        j+=1


# -------------------------------------------
# Pa dobro Boki genije, programeru pocetniku, moj mladi padawanu :)
#
# Ako si vec sortirao listu, gde se nalazi drugi element po velicini :) Ili recimo sedmi po velicini?
#
# U zavisnosti od toga kako je lista sortirana, ne znam sta je po defaultu, od najmanjeg ili najveceg elementa da li krece
#  drugi po velicini ce biti na drugom ili pretposlednjem mestu, tako da je dovoljno da napises
#
# lista[2] ili lista[-2] i to je to, to je taj element
# ------------------------------------------
# Da li bi znao ovo da uradis bez sortiranja.
# --------------------------------------------