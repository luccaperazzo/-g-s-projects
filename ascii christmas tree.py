height = int(input("ingrese altura : "))
s = height
x = " " * s
xd = 1 #ok
while xd < height:
    for i in range(height):
        print(x,"*" * (xd*2))
        s = s - 1
        x = " " * s
        xd = xd + 1
print(" " * (height//2)*2,"**")
    
        