#hangman
words = []
with open('/usr/share/dict/words') as f:
    for line in f:
        words.append(line.strip())
import random
a = random.choice(words)
print(a)
guess = input("ingrese una letra: ")
contador = 5
i = 0
lista = []
long = len(a)
print(long)
while contador > 0:
    if guess == a[i]:
        print("ha ingresado",guess)
        print("correcto")
        lista.append(guess)
        print(lista)
        long=long-1
        print("a la palabra le quedan ",long,"caracteres")
        i = i+1
        guess = input("ingrese una letra: ")

    else:
        print("ha ingresado",guess)
        print("incorrecto, intente de nuevo")
        contador -= 1
        print("le quedan",contador,"intentos")
        guess = input("ingrese una letra: ")
        

        
