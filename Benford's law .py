lista = [3,2,1,5,4,3,3,2,1,1,1,1,1,1,1,1,7,6,6,5,4,3,2,2,1,7,5,4,4,3,3,2,1,1,1,1,1,1,9,7,6,5,5]
lista2 = []
i = 0
for i in lista:
    lista2.append(int(str(i)[0]))
    i += 1
print(lista2)
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
for x in lista:
    if x == 1:
        contador1 += 1
    elif x == 2:
        contador2 += 1
    elif x == 3:
        contador3 += 1
    elif x == 4:
        contador4 += 1
print(contador1)
print(contador2)
print(contador3)
print(contador4)
por = contador1 / len(lista) * 100
print(por,"%")