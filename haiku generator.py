import random
import re
nouns = ["puppy", "car", "rabbit", "girl", "monkey"]
verbs = ["runs", "hits", "jumps", "drives", "barfs"]
adv = ["crazily", "dutifully", "foolishly", "merrily", "occasionally."]
adj = ["adorable", "clueless", "dirty", "odd", "stupid"]
leng = random.randint(1,4)
cantidad = random.randrange(1,5)
for i in range(cantidad):
    oracion = nouns[i]+  " " + verbs[i] +  " " + adv[i] +   "\n " + adj[i]
    print(oracion)



        
        
