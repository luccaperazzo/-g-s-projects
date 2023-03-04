texto = input("ingrese testo a traducir : ")
lista = []
for i in range(len(texto)):
    print(texto[i])
    lista.append(texto[i])
    
print(lista)

def morse(lista):
    for i in lista:
        if i == "a":
            print("*-",end=" ")
        elif i == "b":
            print("-***",end=" ")
        elif i == "c":
            print("-*-*",end=" ")
        elif i == "d":
            print("-**",end=" ")
        elif i == "e":
            print("*",end=" ")
        elif i == "f":
            print("**-*",end=" ")
        elif i == "g":
            print("--*",end=" ")
        elif i == "h":
            print("****",end=" ")
        elif i == "i":
            print("**",end=" ")
        elif i == "j":
            print("*---",end=" ")
        elif i == "k":
            print("-*-",end=" ")
        elif i == "l":
            print("*-**",end=" ")
        elif i == "m":
            print("--",end=" ")
        elif i == "n":
            print("-*",end=" ")
        elif i == "o":
            print("---",end=" ")
        elif i == "p":
            print("*--*",end=" ")
        elif i == "q":
            print("--*-",end=" ")
        elif i == "r":
            print("*-*",end=" ")
        elif i == "s":
            print("***",end=" ")
        elif i == "t":
            print("-",end=" ")
        elif i == "u":
            print("**-",end=" ")
        elif i == "v":
            print("***-",end=" ")
        elif i == "w":
            print("*--",end=" ")
        elif i == "x":
            print("-**-",end=" ")
        elif i == "y":
            print("-*--",end=" ")
        elif i == "z":
            print("--**",end=" ")
        elif i == " ":
            print(" ",end=" ")
        
a = morse(lista)
print(a)
        
        
        