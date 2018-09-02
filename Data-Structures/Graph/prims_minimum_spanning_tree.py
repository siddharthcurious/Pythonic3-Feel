from itertools import permutations
def CountNaturalNumber(n):

    p = permutations(str(n))
    for i in p:
        print(i)



if __name__ == "__main__":

    CountNaturalNumber(100)

