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
