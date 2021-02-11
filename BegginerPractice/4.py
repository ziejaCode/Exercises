'''
Created on 31 May 2020

@author: czarn
'''


word = input()
revword = ""
for w in range(len(word)- 1, -1, -1):
    revword += word[w]
    
if word == revword:
        print(word + " is Palindrome ")
else:
        print(revword + " is Palindrome ")

