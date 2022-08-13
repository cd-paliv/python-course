# recursive functions

# 1
def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

# 2
def binary_search(l,key):
	if len(l) == 0:
		return False
	else:
		mid = len(l) // 2 # position of value in the middle
		if l[mid] == key:
			return True
		elif key < l[mid]:
			return binary_search(l[:mid],key)
		else:
			return binary_search(l[mid+1:],key)




if __name__ == '__main__':
	print(factorial(0))
	l = [10,20,30,40,50,60,70,80,90]
	key = 700
	print(binary_search(l,key))