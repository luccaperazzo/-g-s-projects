import random
# generar grilla con numeros
arr = [[0 for row in range(10)] for column in range(10)]
numeros = random.randint(1,3)
posfila = random.randint(1,9)
posnum = random.randint(1,9)

i = 0
while i < 15:
    arr[posfila][posnum] = numeros
    numeros = random.randint(1,3)
    if posfila % 2 == 0:
        posnum += 1
        posfila = posfila + 1
    elif posfila % 2 != 0:
        posnum += 1
        posfila += 1
    elif posnum >= 10 or posfila >= 10:
        break
    i = i + 1
    print("fila = ",posfila)
    print("pos = ",posnum)

#print   
contador2 = 1
for row in arr:
    print(contador2,": ",end= " ")
    print(" ".join(str(cell) for cell in row))
    contador2 += 1
# poner banderas
flag = True
i = 0
while flag:
    fila = int(int(input("ingrese numero de fila: ")))
    posicion = int(input("ingrese numero de posicion: "))
    arr[fila][posicion] = "B"
    contador1 = 1
    for row in arr:
        print(contador1,": ",end= " ")
        print(" ".join(str(cell) for cell in row))
        contador1 += 1
    if fila == -1:
        print(" ")
        break
# print  
contador = 1
for row in arr:
    print(contador,": ",end= " ")
    print(" ".join(str(cell) for cell in row))
    contador += 1