# 28. Напишите програм за Питхон да бисте пронашли други највећи број на листи.

lista=[1,2,3,4,5,5,6,8,9,7,9,10,10]
lista.sort()

i=len(lista)-1

while i>0:
    if lista[i] > lista[i-1]:
        print ('Drugi najveci broj u listi',lista,'je',lista[i-1])
        break
    else:
        i-=1
