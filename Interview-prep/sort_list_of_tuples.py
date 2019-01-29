from operator import itemgetter
L = [
    (3, "ram", "C"),
    (4, "san", "E"),
    (6, "kate", "G"),
    (5, "hell", "D"),
    (1, "hello", "A"),
    (2, "world", "B")
]

L1 = sorted(L, key=itemgetter(2))

print(L1)

L2 = sorted(L, key=lambda x: x[2])

print(L2)