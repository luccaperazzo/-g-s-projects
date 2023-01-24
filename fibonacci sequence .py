lista = [0,1]
contador = 0
while contador < 50:
    suma = lista[-1] + lista[-2]
    lista.append(suma)
    contador += 1
print(lista)
    