list1 = []
list2 = []
listSon = []
deger = int(input("bir sayi giriniz: "))


for i in range(0, deger):
    if i % 2 != 0 :
        list1.append(i)
    else:
        list2.append(i)
    
list1.extend(list2)

for x in range(len(list1)):
    listSon.append(list1[x] * 2)

for i in range(len(listSon)):
    print(type(listSon[i]))
