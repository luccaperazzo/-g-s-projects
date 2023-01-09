# count the words in  string
import re
string = input("ingrese una oracion: ")
x = re.findall("\s", string)
contador = 1
for i in range(len(x)):
    contador += 1
print("hay",contador,"palabras")
    