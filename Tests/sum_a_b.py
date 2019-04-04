def sum_a_b(numbers, k):
    # numbers = sorted(numbers)
    numbers.sort()
    i = 0
    j = len(numbers) -1

    while i < j:
        if numbers[i] or numbers[j] == k:
            return True
        elif numbers[i] + numbers[j] == k:
            return True
        elif numbers[i] + numbers[j] > k:
            j -=1
        elif numbers[i] + numbers[j] < k:
            i += 1


    return False

if __name__ == "__main__":

    L =  [1,2,6,5,8,3]
    r  = sum(L, 8)
    print(r)
