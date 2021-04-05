#Напишите Питхон програм за уклањање дупликата са листе.

L=[1,2,3,4,5,6,7,8,9,10,2,4,6,8,10]
d=[]

duplikati = set()

for x in L:
    if x not in duplikati:
        d.append(x)
        duplikati.add(x)

print(d)



        
