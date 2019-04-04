def longest_substring(source):
    i = 0
    L = len(source)
    start = 0
    end = 0
    mlen = 0
    map = {}
    sub = ""

    while end < L:
        if not map.get(source[end]):
            map.update({source[end]: 1})
        else:
            clen = end - start
            if clen > mlen:
                mlen = clen
                sub = source[start:end]
            start += 1
        end += 1
    return mlen, sub

if __name__ == "__main__":

    t = "aaabcababcdefghik"
    #t = "anadkumar"
    r = longest_substring(t)
    print(r)