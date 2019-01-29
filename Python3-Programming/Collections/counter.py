from collections import Counter
a = [1,1,1, 2,2,2,3]

count = Counter(a)
print(count)

p = count.most_common(2)
print(p)


