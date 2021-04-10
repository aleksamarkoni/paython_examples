# 25. Напишите Питхон програм за случајно бирање ставке са листе.

import random
lista = [1,2,3,4,5,6]
print(random.choice(lista))

# ----------------------------
# ok ovo random imas vec ugradjeno. ali ako cemo po starom, treba prvo da definises random broj izmedju 1 i len(lista),
# i onda uzmes taj element.
#
# Treba znati kako generisati nasumican broj izmedju 1 i nekog broja
# --------------------------
