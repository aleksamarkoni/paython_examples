#Напишите Питхон програм за бројање броја низова где је дужина низа 2 или
#више, а први и последњи знак су исти са дате листе низова. 
#['абц', 'киз', 'аба', '1221'] 
#Очекивани резултат: 2 

lista = ['абц', 'киз', 'аба', '1221']
n = 0

for j in lista:
    if len(j) > 1 and j[0] == j[-1]:
        n += 1
        print (j)
print(n, 'elemenata')

# ----------------------------------
# he he, bas se ti siris sa ovim -1.
#
# Ovo je dobro sve, ovako treba da izgleda python program, kratko i jasno. Samo imas ovaj print(j), mislim da ti to ne treba
# ---------------------------------
