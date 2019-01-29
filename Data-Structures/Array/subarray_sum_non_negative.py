def sub_array_sum(A, K):

    curr_sum = []
    start_index = 0
    end_index = 0

    for ele in A:
        curr_sum.append(ele)
        end_index += 1

        while sum(curr_sum) > K:
            curr_sum = curr_sum[1:]
            start_index += 1

        if sum(curr_sum) == K:
            return [start_index, end_index-1], True
    return False

if __name__ == "__main__":

    A = [5, 6, 7, 1, 9, 3, 6, 12]
    r = sub_array_sum(A, 22)
    print(r)