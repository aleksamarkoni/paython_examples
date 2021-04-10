# 16. Напишите програм Питхон за генерисање и штампање листе првих и последњих
# 5 елемената где су вредности квадрат бројева између 1 и 30 (оба укључена).

lista = []
for i in range(1,31):
    lista.append(i**2)

print ('Lista',lista)
print('Prvih 5 elemenata',lista[:5])
print('Poslednjih 5 elemenata', lista[-5:])

# --------------------------------------
# Opa Boki, poceo si da sabijas ove rangove :)
# --------------------------------------



