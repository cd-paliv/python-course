# string
# s = ' ' | s = " " | s= """ """
# strings are immutable; which means that if something changes in the variable, then the memory cell in which the variable is saved will change

s1 = "Python"
print(id(s1))

s1 = "Java"
print(id(s1))

# strings is an ordered data structure - it permits indexing and slicing
s2 = "Python sample string"

print(s2[0]) # Indexing: gets the specific char inside the string
print(s2[0:6]) # Slicing: gets te specified part inside the string

# we can also stride the string and get certain values
print(s2[::2]) # from the whole string gets one every two chars
print(s2[::-1]) # from the whole string gets it backwards

print("----------------------")
# 2

# format
num1=100
num2=200
print("num1={}, num2={}".format(num1,num2))

# functions
print(s2.upper())
print(s2.lower())
print(s2.title())

# split
sSplit = "HTML,CSS,Python,Java,Django"
l = sSplit.split(",") # splits the elements between ", " inside the string
print(l)

# join
sJoin = (" ").join(l) # joins in one string every element of the list separated by " sSplit"
print(sJoin)
