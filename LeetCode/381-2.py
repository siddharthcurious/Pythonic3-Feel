def formatWord(words):
    fwords = []
    for word in words:
        fword = 0
        for letter in word:
            fword |= 1 << ord(letter) - ord('a')
        fwords.append(fword)
    return fwords

if __name__ == "__main__":


    A = ["abf", "def", "abf"]
    r  = formatWord(A)
    print(r)