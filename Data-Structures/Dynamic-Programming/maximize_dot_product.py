def maximize_dot_product(A, B):
    if len(A) == len(B):
        dot_product = 0
        for i in range(len(A)):
            dot_product = dot_product + A[i] * B[i]
        return dot_product
    else:
        return max()

if __name__ == "__main__":

    A = [1,2,12,3,6,9]
    B = [3,4,1,2]

    maximize_dot_product(A, B)