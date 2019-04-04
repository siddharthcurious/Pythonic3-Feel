def cmp(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    return (ab > ba) - (ba < ab)

def greater_number(A):
    A1 = sorted(A, cmp=cmp)
    print(A1)

if __name__ == "__main__":

    A = [2, 4, 204, 501, 6, 8]
    greater_number(A)