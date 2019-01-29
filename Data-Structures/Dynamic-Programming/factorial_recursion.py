def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":

    r  = factorial(10)
    print(r)