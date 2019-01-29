def equilibrium_index(A):

    S = sum(A)
    left_sum = 0

    eindex = 0

    for element in A:
        S = S - element
        eindex += 1
        if left_sum == S:
            return eindex - 1
        left_sum += element

if __name__ == "__main__":

    A = [ -7, 1, 5, 2, -4, 3, 0 ]
    r = equilibrium_index(A)
    print(r)