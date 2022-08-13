# user defined functions
# they're used for code reuse, modularity

def value_reverse(value):
	reverse = value[::-1]
	return reverse

s = "Python"
result = value_reverse(s)
print(result)

l = [10,20,30,40,50]
result = value_reverse(l)
print(result)

