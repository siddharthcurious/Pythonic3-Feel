def subarray_sum(A, K):

    curr_sum  = 0
    index = 0

    map = {}

    for ele in A:
        curr_sum += ele
        if curr_sum == K:
            return index

        if curr_sum - K in map:
            return map[curr_sum - K] + 1

        map[curr_sum] = index
        index += 1

    print(map)

if __name__ == "__main__":

    A = [10, 2, -2, -20, 10, 15, 5, 20]
    sum = 25
    r = subarray_sum(A, sum)
    print(r)