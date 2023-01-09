import random
lista = ["piedra","papel","tijera"]
caso1 = random.choice(lista)
caso2 = random.choice(lista)

if caso1 == "piedra":
    if caso2 == "tijera":
        print(caso1,caso2)
        print("Gana piedra")
    else:
        print(caso1,caso2)
        print("perdes o empatas")
    
elif caso1=="papel":
    if caso2 == "piedra":
        print(caso1,caso2)
        print("gana Papel")
    else:
        print(caso1,caso2)
        print("perdes o empatas")

elif caso1 == "tijera":
    if caso2 == "papel":
        print(caso1,caso2)
        print("ganaste negro")
    else:
        print(caso1,caso2)
        print("perdes o empatas nigga")
    