import session16_recursivefunc

# to avoid the results shown in terminal from module imported, we need to check if the call is being made by the module that contains that function defined
# for that we compare __name__ to '__main__'

l = [500,600,700,800,900]
print(session16_recursivefunc.binary_search(l,500))

