def bit_diff(a, b):
    d = a ^ b
    c = 0
    while d:
        if d & 1 > 0:
            c += 1
        d = d >> 1
    return c

def pair_wise_bit_diff(arr):
    sum = 0
    j = 0
    for i in range(len(arr)):
        j = 0
        while j < len(arr):
            sum += bit_diff(arr[i], arr[j])
            j += 1
    return sum

if __name__ == "__main__":

    arr = [1, 3, 5]
    r = pair_wise_bit_diff(arr)
    print(r)