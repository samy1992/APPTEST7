#Developer: Samy1992
#Random1 execise
impor os
from random import randint, uniform, randon
#This functions generates interger numbers
def Z():
    AnsZ = randint(0,100)
    return AnsZ
#This function generates float numbers
def R():
    AnsR = uniform(0,100)
    return AnsR

#Main
os.system("clear")
print("The integer random number is: ", Z())
r = R()
print("The float random number is: ", r)
