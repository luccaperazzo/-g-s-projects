import re
a = [[0 for i in range(7)] for i in range(6)]

for col in a:
    print(" ".join(str(i) for i in col))

contador = 0
azul = "A"
rojo = "R"
aor = input("color rojo o azul kpo: ?")
xd = 0
while xd < 4:
    fila = int(input("ingrese fila: "))
    pos = int(input("ingrese pos : "))
    if a[fila][pos] == 0 and aor == "rojo":
        a[fila][pos] = rojo
    elif aor == "rojo" and a[fila][pos] != 0:
        a[fila+1][pos] == "rojo"
    elif a[fila][pos] == 0 and aor == "azul":
        a[fila][pos] = azul
    elif aor == "azul" and a[fila+1][pos] != 0:
        a[fila+1][pos] = azul
    elif aor == "para":
        break
    else:
        print("ya hay una ficha en esa posicion, ingrese otra.")
    aor = input("color rojo o azul kpo: ?")

for i in range(len(a)):
    for x in range(len(a[i])):
        if (a[i][x] == "R" and a[i][x+1] =="R" and a[i][x+2] =="R" and a[i][x+3]== "R"):
            print("4 en linea")
        elif (a[i][x] == "A" and a[i][x+1] =="A" and a[i][x+2] =="A" and a[i][x+3]== "A"):
            print("4 en linea")
        elif (a[i][x] == "R" and a[i+1][x] =="R" and a[i+2][x] =="R" and a[i+1][x]== "R"):
            print("4 en linea")
        elif (a[i][x] == "A" and a[i+1][x] =="A" and a[i+2][x] =="A" and a[i+3][x]== "A"):
            print("4 en linea")
contador = 1
for row in a:
    print(contador,": ",end= " ")
    print(" ".join(str(cell) for cell in row))
    contador += 1
    
