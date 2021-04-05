# 8. Напишите програм Питхон да бисте проверили да ли је листа празна или не.
i=int(input('Unesite broj i clanove liste'))
lista=[]

for j in range(i):
    k=input()
    lista.append(k)

if len(lista) == 0:
    print('lista je prazna')
else:
    print('Lista',lista,'nije prazna')    


        
