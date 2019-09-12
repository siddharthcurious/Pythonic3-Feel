def getBinary(L, binary):
    if len(binary) < L:
        print(binary)
    if len(binary) == L:
        print(binary)
        return

    getBinary(L, binary+"0")
    getBinary(L, binary+"1")

if __name__ == "__main__":

    getBinary(6, "")