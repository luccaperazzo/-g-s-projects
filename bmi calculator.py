# bmi calculator
age = int(input("ingrese edad: "))
genero = input("ingrese genero: ")
altura = int(input("ingrese altura en cm: "))
peso = int(input("ingrese peso en kg: "))
altura2 = altura / 100
print(altura2)
bmi = peso / (altura2 * altura2)
print(bmi)
bmi1 = True
while bmi1:
    if bmi >= 18.5 and bmi <= 24.9:
        print("bmi es sano")
    elif bmi < 18.5:
        print("muy delgado compa")
    else:
        print("deja de comer, dale?")
    bmi1 = False
        
        