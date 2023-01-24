decimal = int(input("inserte numero decimal : "))
lista = []
while decimal > 0:
    a = decimal % 2
    b = decimal // 2
    lista.append(a)
    decimal = b
lista.reverse()
print(lista)
    