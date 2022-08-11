# if [condition]: 
#	statement
# elif [condition]:
#	statement
# else:
#	statement

num1 = 100
num2 = 200

if num1 > num2:
	print(num1, "is greater")
elif num2 > num1:
	print(num2, "is greater")
else:
	print("Both numbers are equal")

# every non-zero value will be considered as true