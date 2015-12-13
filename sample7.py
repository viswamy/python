#Learning Python

import os

#Remove duplicates in a string

x = 'madammadammadam'
s = set()
for c in x:
    if(c in s):
        continue
    else:
        s.add(c)
        print(c)

print(s)
