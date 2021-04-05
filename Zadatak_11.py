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
