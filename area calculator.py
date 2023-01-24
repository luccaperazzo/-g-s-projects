# area calculator
figura = input("ingrese de que figura quiere sacar el area: ")
if figura == "rectangulo":
    l = int(input("ingrese longitud: "))
    w = int(input("ingrese ancho: "))
    area1 = l * w
    print("el area es: ",area1,"metros al cuadrado")
elif figura == "triangulo":
    lado1 = int(input("ingrese medidas de lado 1: "))
    lado2 = int(input("ingrese medidas de lado 2: "))
    lado3 = int(input("ingrese medidas de lado 3: "))
    area2 = (lado1 + lado2 + lado3) // 2
    print("el area es: ",area2,"metros")
elif figura == "paralelogramo":
    base = int(input("ingrese medidas de la base: "))
    altura = int(input("ingrese medidas de la altura: "))
    area3 = base * altura
    print("el area es : ",area3,"metros al cuadrado")