#Operators in Python

# 1 Arithmetic operators : +, -, *, /, //, %, **
num1 = 10
num2 = 2
print(num1 + num2)
print(num1 / num2) #division always returns double
print(num1 // num2) #gives the result of a division in integer
print(num1 % num2) #MOD of a division
print(num1 ** num2)

# 2 Comparison operators: <, >, <=, >=, ==, !=

# 3 Identity operators: is, is not
num3 = 100
num4 = 100
print(num3 == num4)
print(num3 is num4)

l = [10, 20, 30]
l2 = [10, 20, 30]
print(l == l2) #true because values are equal
print(l is l2) #false because the memory locations are different

# 4 Assignment operators : =, +=, -=, *=, /=

# 5 Bitwise operators : &, |, ^, <<, >>
num5 = 2
num6 = 1
print(num5 & num6) #returns 0 because it applies the logic function AND to the bits values of the variables (num5 = 2 = 10)
print(num5 | num6) #returns 3 because it applies the logic function OR
print(num5 >> num6) #shifts the value of the variables in bits

# 6 Logical operators : and, or, not
print(10==15 and 20==20)
print(not(10==15 and 20==20))

# 7 Membership operators : in, not in
l3 = [10, 20, 30]
print(30 in l3)
s = "Python string"
print("Python" in s) #true
print("python" in s) #false
