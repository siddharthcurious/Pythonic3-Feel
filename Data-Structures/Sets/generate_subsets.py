def getSubsets(A, subs):

    for e in A:
        subs.add(e)
        getSubsets(A[1:], subs)
        if e in subs:
            subs.remove(e)

if __name__ == "__main__":

    A = [1, 2, 3]
    getSubsets(A, set())