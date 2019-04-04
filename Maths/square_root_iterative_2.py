def square_root(N):
    i = 0
    result = 0
    while result <= N:
        result = i * i
        if result < N:
            i += 1
        else:
            break
    return i

if __name__ == "__main__":

    N = 225
    r  = square_root(N)
    print(r)