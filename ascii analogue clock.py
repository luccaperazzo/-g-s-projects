import datetime
x = datetime.datetime.now()
b = x.time()
#clock body
def setface():
    clockstring = ""
    clockstring = clockstring + "   ~-------------~    " + chr(10) 
    clockstring = clockstring + " ('..'11..12..1'..')  " + chr(10)
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :10            2: | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :9      @      3: | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :8             4: | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + " ('..'7...6...5'..')  " + chr(10);
    clockstring = clockstring + "   ~-------------~    " + chr(10);
    list1 = list(clockstring)
    return list1

print(b)
hours = int(str(b)[:2])
minutes = int(str(b)[3:5])
seconds = int(str(b)[6:8])

def sethour(hours, clockchar):

    if (hours == 13):
        clockchar[104] = "/"

    if (hours == 14):
        clockchar[106] = "/" 
        
    if (hours == 15):
        clockchar[149] = "----" 
        
    if (hours == 16):
        clockchar[173] = "\\"   
        
    if (hours == 17):
        
        clockchar[172] = "\\" 

    if (hours == 18):

        clockchar[171] = "|" 
        
    if (hours == 19):
        clockchar[192] = "/" 
        
    if (hours == 20):
        clockchar[169] = "/" 
        
    if (hours == 21):

        clockchar[145] = "---" 
        
    if (hours == 22):

        clockchar[122] = "\\" 
        
    if (hours == 23):
        clockchar[125] = "\\" 
        
    if (hours == 00):
        clockchar[125] = "|" 
    return clockchar

def setminutes(minutes, clockchar):
    if minutes > 0 and minutes <= 5:
        clockchar[104] = "/"
    elif minutes > 5 and minutes<= 10:
        clockchar[106] = "/"
    elif minutes > 10 and minutes<= 15:
        clockchar[149] = "----"
    elif minutes > 15 and minutes<= 20:
        clockchar[173] = "\\"
    elif minutes > 20 and minutes<= 25:
        clockchar[172] = "\\"
    elif minutes > 25 and minutes<= 30:
        clockchar[171] = "|"
    elif minutes > 30 and minutes<= 35:
        clockchar[192] = "/"
    elif minutes > 35 and minutes<= 40:
        clockchar[169] = "/"
    elif minutes > 40 and minutes<= 45:
        clockchar[145] = "---" 
    elif minutes > 45 and minutes<= 50:
        clockchar[122] = "\\" 
    elif minutes > 50 and v<= 55:
        clockchar[125] = "\\"
    elif minutes > 55 and minutes<= 60:
        clockchar[125] = "|"
    str2 = "".join(clockchar)
    return str2

xd = sethour(hours,setface())
lolo = setminutes(minutes,xd)
print(lolo)