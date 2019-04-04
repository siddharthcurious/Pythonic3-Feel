def pancake_flipper(seq, k):
    seq = list(seq)
    i = 0
    L = len(seq)
    n = 0
    while i < L:
        if seq[i] == "-" and i + k <= L:
            j = i
            for _ in range(k):
                if seq[j] == "-":
                    seq[j] = "+"
                elif seq[j] == "+":
                    seq[j] = "-"
                j += 1
            n += 1
        i += 1
    for c in seq:
        if c == "-":
            return "IMPOSSIBLE"
    return n

if __name__  == "__main__":

    n = int(input())
    for i in range(n):
        s, k = input().split()
        k = int(k)
        r = pancake_flipper(s, k)
        print("Case #{}: {}".format(i+1, r))