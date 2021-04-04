# Najveci elemenat liste

broj_elemenata = int(input('Unesite broj elemenata liste'))

if broj_elemenata == 1:
    print ('Broj',broj_elemenata,'je jedini elemenat liste')

# Kako ovde zaustaviti program?

lista_list = []

prvi_elemenat = int(input('Unesite 1 . elemenat liste'))
lista_list.append(prvi_elemenat)

najveci = lista_list[0]

for i in range (broj_elemenata-1):
    print ('Unesite',i+2,'. elemenat liste')
    j = int(input())
    lista_list.append(j)
    if lista_list[i+1] > najveci:
        najveci = lista_list[i+1]
      
print ('Najveci elemenat liste', lista_list,'je', najveci)






        
