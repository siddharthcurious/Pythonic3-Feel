def sub_array_sum(A, K):

    curr_sum = []
    curr_sum.append(A[0])
    start_index = 0
    end_index = 0

    for ele in A[1:]:
        curr_sum.append(ele)
        end_index += 1
        if sum(curr_sum) > K:
            curr_sum = curr_sum[1:]
            start_index += 1
        if sum(curr_sum) == K:
            return [start_index, end_index]

if __name__ == "__main__":

    A = [5, 6, 7, 1, 9, 3, 6, 2]
    r = sub_array_sum(A, 17)
    print(r)