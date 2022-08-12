# set
# mutable datastructure
# all the elements should be unique and are unordered
# immutable elements in the set - int, float, tuple, str

s = {10,20,30,40}
print(s)

# add elements
s.add(500)
print(s)

s2 = {40, 50, 60, 70, 80}
s.update(s2) # is the same as : s = s.union(s2)
print(s)

# delete elements
# pop - remove - discard - clear - del
aux = s.pop()
print(s, aux)

s.remove(10) # same as :  s.discard
print(s)

s.clear()
print(s)