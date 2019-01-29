def pair(N, M, aa, bb):
    sum = {}
    index = []
    for i in range(N):
        for j in range(M):
            if not sum.get(aa[i]+bb[j]):
                sum.update({aa[i]+bb[j]: (i, j)})
                index.append((i, j))
    return index

if __name__ == "__main__":

    N, M = [int(item) for item in input().split()]
    aa = [int(item) for item in input().split()]
    bb = [int(item) for item in input().split()]
    r = pair(N, M, aa, bb)
    for i in range(N+M-1):
        print(r[i][0], r[i][1])

