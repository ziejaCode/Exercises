'''
Created on 30 May 2020

@author: czarn
'''

num = int(input())
l = []
for d in range(1, num+1):
    if num%d == 0:
        l.append(d)
print(l)