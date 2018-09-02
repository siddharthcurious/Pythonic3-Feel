from itertools import permutations

def CountNaturalNumber(n):
    count = 9
    for num in range(10, n+1):
        perms = permutations(str(num))
        perms_set = set()
        for p in perms:
            number = int("".join(p))
            perms_set.add(number)
        for ele in perms_set:
            if ele > num:
                count = count + 1
        if len(perms_set) == 1:
            count = count +1
    return count

if __name__ == "__main__":
    r = CountNaturalNumber(100)
    print(r)

