# 26. Напишите програм за питхон да бисте проверил да ли су две листе кружно
# идентичне. 

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

l1=list1[:]
l2=list2[:]
l3=list3[:]

l1.sort()
l2.sort()
l3.sort()


if l1==l2:
    print('Liste',list1,'i',list2,'su kruzno identicne')
else:
    print('Liste',list1,'i',list2,'nisu kruzno identicne')

if l2==l3:
    print('Liste',list2,'i',list3,'su kruzno identicne')
else:
    print('Liste',list2,'i',list3,'nisu kruzno identicne')
