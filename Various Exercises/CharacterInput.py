'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.
'''
import time

name = input("Hello ")
age = input("How old are you? ")
copies = input("how many copies do your want")

for i in range(int(copies)):
    # get todays date and format it
    print("Hey {0} your 100th birthday will be at {1}".format(name, (time.localtime()[0] + (100 - int(age)))))
    #print("dsfsdkfljsd")
