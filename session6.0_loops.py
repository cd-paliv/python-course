# Iterable datatypes: str, list, tuple, dict, set

#for [variable] in [iterable datatype]:
#	statements

l = [10, 20, 30, 40, 50]
sum = 0
for value in l:
	sum += value
print(sum)

# range(5) = 0 1 2 3 4
# range(10,100) = 10 11 12 ... 99
# range(10,100,5) = 10 15 20 25 30 35 ... 95 100

sum2 = 0
for value in range(0,20,5):
#	print(value)
	sum2 += value
print(sum2)

# break / continue
l = [10,20,30,40,50]
key = 400

for value in l:
	if value == key:
		print("Element found")
		break
	else:
		continue #specifies that the program should continue
else: #else in for is used to represent the situation in which the break inside the for is never executed
	print("Element not found")

# enumerate
for index, value in enumerate(l): #enumerate provides an index for every value in the datatype
	if value == 40:
		print("Element found at index:",index)
		break
	else:
		continue
else:
	print("Element not found")