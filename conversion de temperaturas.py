def fahrenheit(celcius):
    final = (celcius * 1.8) + 32
    return final

def celsius(fahren):
    final = (fahren-32)*5/9
    return final

def kelvin1(fahren):
    final = ((fahren-32)*5/9) +273
    return final
def kelvin2(cel):
    final = cel + 273
    return final
    

    
    
    
    
jeje = input("desea convertir numero a fahren ,a calsius o a kelvin?: ")
if jeje == "celsius":
    n = int(input("inserte numero en fahren"))
    fafa  = celsius(n)
    print(fafa)
elif jeje == "fahrenheit":
    l = int(input("inserte numero en celcius: "))
    fefe = fahrenheit(l)
    print(fefe)
elif jeje == "kelvin":
    lele = input("desea convertir desde celsius o farhren?: ")
    if lele == "fahren":
        n = int(input("inserte numero en fahren"))
        print(kelvin1(n))
    elif lele == "celsius":
        l = int(input("inserte numero en celcius: "))
        print(kelvin2(l))

        
        
    

