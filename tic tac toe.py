import random
tic = [[1,3,5],
       [6,9,7],
        [2,1,5],]
for i in tic:
    print(i)
         
uno = random.randint(0,2)
dos = random.randint(0,2)
inp = input("ingrese X o O: ")
pos = int(input("ingrese fila :"))
pos1 = int(input("ingrese celda : "))
a = list(filter(lambda e: e[0]==e[1]==e[2], zip(tic[0],tic[1],tic[2])))
 
while len(a) != 1 and tic[0][0] != tic[1][1] != tic[2][2] and tic[0][2] != tic[1][1] != tic[2][0]:
    for x in range(len(tic)):
        for i in tic[x]:
            tic[pos][pos1] = inp
    for i in tic:
        print(i)
    a = list(filter(lambda e: e[0]==e[1]==e[2], zip(tic[0],tic[1],tic[2])))
    inp = input("ingrese X o O: ")
    pos = int(input("ingrese fila :"))
    pos1 = int(input("ingrese celda : "))
print("Ganaste rrope")
            

