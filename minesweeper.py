import random
width = int(input("how wide "))
height = int(input("how tall "))
grid = []
mines = 10
listanumeros = ["1","2","3"]
height2 = height * height
i = int(0)
for i in range(width):
    grid.append("*")
for i in range(height):
    print(grid)
print("la grid s")
random1 = random.randrange(0,len(grid))
random2 = random.choice(listanumeros)
j = 0
while j < mines:
    grid[random1] = random2
    j = j + 1
