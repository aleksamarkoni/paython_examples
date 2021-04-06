# 17. Напишите Питхон програм за генерисање и штампање листе, осим првих 5
# елемената, где су вредности квадрат бројева између 1 и 30 (оба укључена).

lista = []
for i in range(1,31):
    lista.append(i**2)

print ('Lista',lista)
print('Lista bez prvih 5 elemenata',lista[5:])



