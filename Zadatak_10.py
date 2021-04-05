# 10. Напишите програм Питхон да бисте пронашли листу речи које су дуже од н
# са дате листе речи.
lista=['Aco','Marina','Kalina','Hristina','Luka','Anja','Danka','Bojan']
n=int(input('Duzina reci?'))
k=0
reci=set()

for i in lista:
    if len(i) > n:
        reci.add(i)
        k=k+1
        
if k==0:
    print('Lista',lista,'ne sadrzi reci duze od',n,'slova')
else:
    print ('Reci iz liste',lista,'duze od',n,'slova su:',reci)
