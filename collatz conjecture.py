#collatz conjecture
n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese otro numero: "))
while n1 != 1:
    if n1 % 2 != 0:
        ecuacion = (n1 * 3 ) + 1
        print("n1 :",ecuacion)
        n1 = ecuacion
    elif n1 % 2 == 0:
        ecuacion2 = n1 // 2
        print("n1:",ecuacion2)
        n1 = ecuacion2
while n2 != 1:        
    if n2 % 2 != 0:
        ecuacion3 = (n2 * 3 ) + 1
        print("n2 :",ecuacion3)
        n1 = ecuacion3
    if n2 % 2 == 0:
        ecuacion4 = n2 // 2
        print("n2:",ecuacion4)
        n2 = ecuacion4