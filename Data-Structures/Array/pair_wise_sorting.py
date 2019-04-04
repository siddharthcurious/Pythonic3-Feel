import operator
array = [(1, 'a'), (2, 'b'), (5, 'r'), (3, 'a'), (-7, 'k')]
s = sorted(array, key=operator.itemgetter(0))
print(s)

array = [(1, 'a'), (2, 'b'), (5, 'r'), (3, 'a'), (-7, 'k')]
s = sorted(array, key=lambda x:x[0], reverse=True)
print(s)
