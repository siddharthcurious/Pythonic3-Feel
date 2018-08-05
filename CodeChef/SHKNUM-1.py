def is_power_of_two(n):
    if n == 1:
        return True
    if n & (n - 1) == 0:
        return True
    return False

def power(n):

    if not is_power_of_two(n):
        return -1

    c = -1
    while n:
        y = n & 1
        n = n >> 1
        c = c + 1
        if y:
            return c

def min_operations(n):
    pass


if __name__ == "__main__":

    T = int(input())

    for _ in range(0, T):

        n = int(input())
        m  = min_operations(n)
        print(m)