# 23. Напишите Питхон програм како бисте поравнали плитку листу.


lista = [[2,4,3],[1,5,6], [9], [7,9,0]]
temp=[]
nova_lista=[]

for i in range (len(lista)):
    temp=lista[i]
    j=len(temp)
    for k in range (j):
        nova_lista.append(temp[k])

print ('Lista pre poravnavanja')
print (lista)
print ('Lista posle poravnavanja')
print (nova_lista)


# ---------------------
# moze ovo malo lepse
#
# lista = [[2,4,3],[1,5,6], [9], [7,9,0]]
# nova_lista=[]
#
# for l in lista:
#     nova_lista = nova_lista + l
#
# print ('Lista pre poravnavanja')
# print (lista)
# print ('Lista posle poravnavanja')
# print (nova_lista)
#
# Sta se ovde desava, sa ovim for l in lista, ti kazes ajde da prodjemo kroz sve elemente iz lista i svaki nazovi l.
# ovde ce l biti u sustini jedan od ovih podlista.
# I onda samo kazes nadovezi tu podlistu na novu_listu. U pythonu mozes da koristis + izmedju dve liste i on zna sta treba da uradi
# Samo nemoj da koristis nova_lista += l, jer += je malo drugaciji i tu ce vec da krene da se buni (advance topic)
#
# Godina proizvodnje :)
#
# Uvek prvo prveri da li imas neku gotovu funkciju koja ti radi posao, a verovatno ima, pre nego sto krenes da pises svoje.
# ----------------------
