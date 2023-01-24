#factorial of 100
import numpy as np
mylist = []
cien = 100
i = cien - 1
while i > 0:
    mylist.append(i)
    i = i - 1
result = np.prod(mylist)
print(result)
