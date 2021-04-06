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
