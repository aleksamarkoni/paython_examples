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
