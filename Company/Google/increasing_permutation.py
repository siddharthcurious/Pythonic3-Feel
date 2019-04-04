def increasing_permutation(L, k, string):
    if len(string) == k:
        print(string)
        return
    else:
        for i in range(len(L)):
            increasing_permutation(L[i+1:], k, string+str(L[i]))

if __name__ == "__main__":

    L = [1, 2, 3, 4, 5]
    k = 4
    increasing_permutation(L, k, "")