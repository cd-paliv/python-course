l = [100, 200, 300, 400, 500]

print(sum(l))
print(max(l))
print(min(l))

numF = 25.5555
print(round(numF,2))

# math functions
import math

l = [0.1] * 10 # creates a list with 10 nodes with the value 0.1
print(l)

print(sum(l)) # 0.999999...
print(math.fsum(l)) # 1.0 - round

print(math.sqrt(25))

print(math.factorial(5))

print(math.pow(10,2))

num = 45.5556
print(math.modf(num)) # returns the separate decimal and integer values 

d, i = math.modf(num)
print(i) # prints the integer value of num
print(d) # prints the decimal value of num


# random function
import random

print(random.randint(10,100)) # random int
print(random.uniform(10,20)) # random float

l = [1,2,3,4,5,6]
print(random.choice(l))

