def subset_sum(set, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if sum < set[n]:
        return subset_sum(set, n-1, sum)
    return subset_sum(set, n-1, sum - set[n]) or subset_sum(set, n-1, sum)

if __name__ == "__main__":

    set = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(set) - 1
    r = subset_sum(set, n, sum)
    print(r)