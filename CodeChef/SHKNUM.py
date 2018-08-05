def powerOfTwo(n):
    if n == 1:
        return True
    if n & (n - 1) == 0:
        return True
    return False

def minOperation(n):

    if n == 0:
        return 2
    if n == 1:
        return 1

    x = 2
    p = 0
    y = 0
    prev = 0
    while y < n:
        prev = y
        y = x ** p
        p = p + 1

    diff = n - prev

    if powerOfTwo(diff):
        return 0

    minus_one = 0
    d1 = diff
    while  powerOfTwo(d1) is False:
        d1 = d1 - 1
        minus_one = minus_one + 1

    plus_one = 0
    d2 = diff
    while powerOfTwo(d2) is False:
        d2 = d2 + 1
        plus_one = plus_one + 1

    if minus_one > 0 and plus_one > 0:
        return min(plus_one, minus_one)
    else:
        return max(plus_one, minus_one)


if __name__ == "__main__":

    T = int(input())
    for _ in range(0, T):

        n = int(input())
        print(minOperation(n))



