# 4.Najmanji elemenat liste

broj_elemenata = int(input('Unesite broj elemenata liste'))

lista_list = []

prvi_elemenat = int(input('Unesite 1 . elemenat liste'))
lista_list.append(prvi_elemenat)

najmanji = lista_list[0]

for i in range (broj_elemenata-1):
    print ('Unesite',i+2,'. elemenat liste')
    j = int(input())
    lista_list.append(j)
    if lista_list[i+1] < najmanji:
        najmanji = lista_list[i+1]
      
print ('Najmanji elemenat liste', lista_list,'je', najmanji)






        
