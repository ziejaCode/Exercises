'''
Created on 30 May 2020

@author: czarn
'''
import random


l1, l2 = [],[]

for e in range(random.randrange(9)):
    l1.append(e)
    
for i in range(random.randrange(9)):
    l2.append(i)

print(l1)
print(l2)


l3 = set()



for e in l2:
    for a in l1:
        if e == a:
            l3.add(e)            
print(l3)
