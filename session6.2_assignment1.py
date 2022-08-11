# 1
# Write a Python program to find those numbers which are divisible by 7
# and 5, between 1500 and 2700 (both included)
print("--------------1--------------")
sum = 0
for value in range(1500,2701):
	if (value % 5 == 0) & (value % 7 == 0):
		print(value)
		sum += 1

print("Amount of numbers divisibles by 5 and 7:",sum)


# 2
# Write a Python program to count the number of even and odd numbers
# from a series of numbers
print("--------------2--------------")
even = 0
odd = 0
l = [1,2,3,4,5,6,7,8,9]
for value in l:
	if value % 2 == 0:
		even += 1
	else:
		odd += 1
print("Amount of even numbers:", even)
print("Amount of odd numbers:", odd)


# 3
# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" and for multiples of five print "Buzz".
# For numbers which are multiples of both thee and five print "FizzBuzz".
print("--------------3--------------")
count = 1
Fizz = 0
Buzz = 0
FizzBuzz = 0
while count <= 50:
	if count % 3 == 0:
		if count % 5 == 0:
			#print("FizzBuzz")
			FizzBuzz += 1
		else:
			#print("Fizz")
			Fizz += 1
	elif count % 5 == 0:
		#print("Buzz")
		Buzz += 1
	count += 1

print("Amount of Fizz:",Fizz)
print("Amount of Buzz:",Buzz)
print("Amount of FizzBuzz:",FizzBuzz)


# 4
# Write a Python program to calculate the sum and average of n int numbers
print("--------------4--------------")
sum3 = 0
count2 = 1
n = 10
while count2 <= n:
	sum3 += count2
	count2 += 1

print("Sum:", sum3)
print("Average:",sum3/count2)


# 5
# Write a Python program to calculate the factorial of a number
print("--------------5--------------")
number = 4
f = 1
for value in range(1,number+1):
	f *= value
print("Factorial of",number,":",f)