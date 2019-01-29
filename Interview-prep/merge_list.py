import itertools

L = [[1,2,3], [4,5], [6,7,8], [9,10,11]]

merged = itertools.chain.from_iterable(L)

for a in merged:
    print(a)