from functools import reduce
import operator

L = [1,2,3,4,5,6,7,8,9,10]

L1 = map(lambda x:x**2, L)
print(L1)
for a in L1:
    print(a)

L2 = filter(lambda x: x%2==0, L)
print(L2)
for b in L2:
    print(b)

V1 = reduce(lambda x, y:    x + y, L)
print(V1)


L = ["geeks", "for", "geeks"]

L3 = reduce(operator.concat, L)
print(L3)