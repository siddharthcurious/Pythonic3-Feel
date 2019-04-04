def square_root_binary_search(N, precision):
    start = 0
    end = N

    ans = 0
    while start <= end:
        mid = (start + end)/2

        if mid * mid == N:
            ans = mid
            break
        if mid * mid < N:
            start += 1
            ans = mid
        else:
            end = mid - 1

    increment = 0.1
    for i in range(precision):

        while ans * ans <= N:
            ans += increment



if __name__ == "__main__":

    N = 40
    precision = 5
    r = square_root_binary_search(N, precision)
    print(r)