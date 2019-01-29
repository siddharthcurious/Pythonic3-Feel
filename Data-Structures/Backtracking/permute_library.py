from itertools import permutations

def permute(string):
    perms = permutations(string)
    for e in perms:
        print(e)

if __name__ == "__main__":

    permute("SAN")