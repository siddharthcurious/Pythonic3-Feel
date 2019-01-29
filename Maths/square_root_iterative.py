def square_root_iterative(n):
    x = n
    y = 1
    while(x > y):
        x = (x + y) / 2
        y = n / x
    return x

if __name__ == "__main__":

    num  = square_root_iterative(500)
    print(num)