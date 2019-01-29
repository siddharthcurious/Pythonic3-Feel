def sub_array_sum(A, K):

    curr_sum = 0
    start_index = 0
    end_index = 0

    for ele in A:
        curr_sum += ele
        end_index += 1

        while curr_sum > K:
            curr_sum -= A[start_index]
            start_index += 1

        if curr_sum == K:
            return [start_index, end_index-1]
    return False

if __name__ == "__main__":

    A = [5, 6, 7, 1, 9, 3, 6, -9, -12, 12]
    r = sub_array_sum(A, 21)
    print(r)