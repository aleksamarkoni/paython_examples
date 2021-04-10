# 20. Напишите програм за Питхон који приступа индексу листе.

lista = [5, 15, 35, 8, 98]

for i in range(len(lista)):
    print('Indeks',i,'Elemenat',lista[i])


# -------------------------------
# dobro ovo je ok, ali ajde da vidimo da li mozda vec ima nesto u Pythonu za ovo
#
# ako ti ne treba index, onda obicno pises
#
# for e in lista:
#     print(e)
#
# ovo ce da ti ispise sve elemente liste, ali sta ako recimo zelis da istampas samo elemente ciji je indeks deljiv sa tri,
# a da opet koristis ovaj slican for. Naravno mozemo da koristiom for petlju sa rangom i da pristupamo elementima ali ajde,
# da vidimo da li moze bez toga.
#
# for index, item in enumerate(items):
#     print(index, item)
#
# ima nesto u pythonu sto se zove enumerate(list), koji ce od liste da da za svaki element vrati par (index, item), tako da
# mozemo to da koristimo, sto je mozda zgodnije, nego da radimo list[i] svaki put. ovako imamo posebno i index i item.
#
# Ajde da uporedimo
#
# for i in range(len(list)):
#     if (i // 2 != 0):
#         print(list[i])]
#
# for i, e in enumerate(list): # nema len(list)
#     if (i // 2 != 0):
#         print(e) # nema list[i]
#
# Pa malo sam brze napisao ovaj drugi primer :/ Cisto da znas da ima i ovo
# -----------------------------------------------------------------------------
