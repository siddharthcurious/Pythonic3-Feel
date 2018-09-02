from random import shuffle

x = ["hey", "man", "how", "are", "you"]

for _ in range(10):
    shuffle(x)
    print(x)