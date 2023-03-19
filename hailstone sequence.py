user = int(input("ingreses un numero: "))
def x(user):
    while user != 1:
        if user % 2 == 0:
            user = user // 2
            print(user)
        elif user % 2 != 0:
            user = (user * 3 )+ 1
            print(user)
                
print(x(user))
