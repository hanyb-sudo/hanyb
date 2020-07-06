import itertools

#排列组合

mylist = list(itertools.product("0123456789", repeat=3))
print(mylist)
print(len(mylist))
