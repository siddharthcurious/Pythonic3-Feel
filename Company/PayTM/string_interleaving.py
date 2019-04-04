def interleaving(str1, str2, target, L1, L2, i):
    if L1 == 0 and L2 == 0:
        print("".join(target))

    if L1 != 0:
        target[i] = str1[0]
        print("str1={} str2={} target={}, L1={}, L2={}, i={}".format(str1, str2, "".join(target), L1, L2, i))
        interleaving(str1[1:], str2, target, L1 - 1, L2, i + 1)

    if L2 != 0:
        target[i] = str2[0]
        print("str1={} str2={} target={}, L1={}, L2={}, i={}".format(str1, str2, "".join(target), L1, L2, i))
        interleaving(str1, str2[1:], target, L1, L2 - 1, i + 1)

if __name__ == "__main__":

    str1 = "ABC"
    str2 = "DE"
    L1 = len(str1)
    L2 = len(str2)
    target = [''] * (L1 + L2)
    interleaving(str1, str2, target, L1, L2, 0)