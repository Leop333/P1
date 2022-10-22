#my tris)
a=int
b=int
print("give input")
input(a)
input(b)
sum=a+b

print(sum)

#0
a = int(input())
b = int(input())
print(a + b)

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#1
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # exponentiate
print(37 / 3)  # division
print(37 // 3)  # division integer
        
print(37 % 3)  # modulo (division residuals)
        
        
name = input()  # 
print('Hi ' + name + '!')


#Problem «Square»
print(" input base and power")
a = int(input())
b = int(input())
print(a ** b)


#Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. 
#Every number is given on a separate line.
print(" input base and height")
a = int(input())
b = int(input())
print(a * b)
pip install numpy
import numpy as np


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high")


#3
#Write a Python program which accepts a sequence of comma-separated numbers 
#from user and generate a list and a tuple with those numbers.

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)



#4
#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)


import math


x = math.ceil(4.2)
print(x)
print(math.ceil(1 + 3.8))
