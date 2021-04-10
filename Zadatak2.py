#Mnozenje unetih elemenata liste

broj_elemenata = int(input('Unesite broj elemenata liste'))

lista_list = []

proizvod = 1

for i in range (broj_elemenata):
    print ('Unesite',i+1,'. elemenat liste') # lint problemi ovde, treba da se dodaju spacovi
    j = int(input())
    lista_list.append(j)
    proizvod = proizvod * j

print ('Proizvod elemenata liste', lista_list,'je',proizvod)

# ----------------------------------
# Ako zanemarimo Lint koji je problem u svakom zadatku, ali to cu pripisati onom idle editoru, ovaj zadatak je dobar.
# ---------------------------------
# Ime lista_list nije dobro, mislim lista_list, kao Bojan_boki :)
# ------------------------------------