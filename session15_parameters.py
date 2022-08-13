# parameters
l = [10,20,30,40,50]

# positional arguments
def linear_search(l,key):
	for value in l:
		if key == value:
			return True
	else:
		return False

key = 30
result = linear_search(l,key)
print(result)

# default arguments
import random
def gen_password(length=5): # default value
	upper = chr(random.randint(65,90)) # from A to Z
	lower = chr(random.randint(97,122)) # from a to z
	digit = random.randint(1000,9999)
	password = upper + lower + str(digit)
	l = random.sample(password,length)
	return ("").join(l)

result = gen_password(3)
print(result)

# keyword arguments
def validate(username,password):
	if username == "cdpaliv" and password == "cd1234":
		print("Valid")
	else:
		print("Invalid")

validate("cdpaliv","cd1234")
validate(password="cd1234",username="cdpaliv")

# variable length positional arguments
def add_value(*args):
	l = []
	for value in args:
		l.append(value)
	return l

result = add_value(100,200,300)
print(result)
result = add_value(100,200,300,400,500,600,700,800,900,1000)
print(result)

# variable length keyword argument
def get_details(**kwargs): # keywordarguments: puts the parameters in a dictionary
	print(kwargs)

get_details(name="AB",email="AB@gmail.com",contact=2214783224,dob="12-05-1890")
get_details(name="AB",email="AB@gmail.com",dob="12-05-1890")
get_details(name="AB",contact=2214783224,dob="12-05-1890")