#Basic Calc to junior users
#Developer: samy1992
#libraries ##########################################################
import os
#####################################################################
a = 5
b = 6

#Functions############################################################
def calc(x, y):
    suma = x + y
    print("La suma es: ", suma)

#Main#################################################################
os.system("clear")
print("Press number 1: ")
a = int(input())

b = int(input("Press number 2: "))

calc(a,b)    
