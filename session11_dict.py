# dictionary
# mutable and unordered datastructure
# cointains unique keys that allow to get a certain value inside
# keys can be int, float, str, tuple

d = {"emp_id":101,"name":"ABC", "email":"ABC@gmail.com"}

# add elements
d["number"] = 123456789
print(d)

# to obtain a value, we have to use the key
print(d["emp_id"])

# functions
print(d.get("emp", "Key does not exist")) # prints the value or, if the key does not exist, prints the str

print(d.keys()) # prints the keys in the dictionary
print(d.values())# prints the values in the dictionary
print(d.items()) # prints the keys and the values in the dictionary

# to create a dictionary from lists :
l1 = [1,2,3,4,5]
l2 = [1,4,9,16,25]

d1 = dict(zip(l1,l2)) # creates a dict in which the keys are formed by the elements of the first list, and the values of the second
print(d1)

d3 = dict.fromkeys(l1) # creates a dict in which the keys are formed by the elements of the list, and the values are set to 'None'
print(d3) 

# merge dictionaries
d4 = {1:1,2:4}
d5 = {3:9,4:16,5:25}

d4.update(d5)
print(d4)

# delete elements
# pop
aux = d4.pop(2) # deletes the 2 element of the dict
print(d4, aux)

aux = d4.popitem() # deletes a random element of the dict
print(d4, aux)