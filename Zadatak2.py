#Mnozenje unetih elemenata liste

broj_elemenata = int(input('Unesite broj elemenata liste'))

lista_list = []

proizvod = 1

for i in range (broj_elemenata):
    print ('Unesite',i+1,'. elemenat liste')
    j = int(input())
    lista_list.append(j)
    proizvod = proizvod * j

print ('Proizvod elemenata liste', lista_list,'je',proizvod)






        
