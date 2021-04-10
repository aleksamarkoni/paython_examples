# 3.Najveci elemenat liste

broj_elemenata = int(input('Unesite broj elemenata liste'))

# ---------------------------------------
# sta ako je ovde broj_elemenata < ili = 0
# ---------------------------------------
if broj_elemenata == 1:
    print ('Broj',broj_elemenata,'je jedini elemenat liste')
    
# Kako ovde zaustaviti program?

# -----------------------------------------------
# Ima vise nacina da se zavrsi program, o tome cemo pricati
# ------------------------------------------------

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


# -------------------------------------------------
# pa ovo je ok, samo eto da razmislis sta bi moralo u programu da se promeni da si ovu for petlju napisao ovako
# for i in range(1, broj_elemenata - 1):
# --------------------------------------------------
# moram samo napomenuti da postoji i ugradjeni operator max(lista) koji vraca najveci element.
# u tom slucaju, uneses elemente liste i prosledis listu, i on ti izracuna koji je max
# --------------------------------------------------



        
