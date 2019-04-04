def isSubsetSum(numbers, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if numbers[n] > sum:
        return isSubsetSum(numbers, n-1, sum)

    return isSubsetSum(numbers, n-1, sum) or isSubsetSum(numbers, n-1, sum-numbers[n])

if __name__ == "__main__":

    numbers = [3, 34, 4, 12, 5, 2]
    sum = 11
    L = len(numbers)
    r = isSubsetSum(numbers, L-1, sum)
    print(r)
