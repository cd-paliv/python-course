# list
# list are mutable
# it permits adding, updates and deletion, besides ordered, indexing and slicing
# its a heterogeneous datatype

l = [10,20,30,40,"Python","Java",[100,200,300]]
print(l[6][0])
print(type(l))

# adding elements
l.append(600) # adds 600 to the end of the list
print(l)
l.extend([700,800,900])
print(l)

# copying list
l2 = l.copy() # copies the elements in l and puts it in another memory cell
print(l2)

# update elements
print(l2[6])
l2[6] = 500
print(l2[6])

# delete elements
aux = l.pop() #deletes the last element of the list and saves it in aux
l.remove("Python") #deletes the exact element from the list
l.clear() #deletes every element from the list
# del l - deletes the list from memory
print(l)

# ordered
l = [50,20,10,30,40]
l.sort()
print(l)
