# tuple
# immutable datastructure
# allows ordered, indexing and slicing

t = (10,20,30,40)
l = [10,20,30,40]
for t in enumerate(l): # generates a tuple that contains the index AND the values in the list
	print(t)

# we can convert a list to a tuple
t = tuple(l)
print(t)

# or a tuple to a list
t2 = ("a","b","c",100)
l2 = list(t2)
print(l2)
