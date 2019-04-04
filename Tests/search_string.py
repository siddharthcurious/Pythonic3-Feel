def search(main, pattern):
    c = 0
    if pattern in main:
        c +=1
    return c

if __name__ == "__main__":

    main = "Canadian banana"
    pattrn = "ana"
    r = search(main, pattrn)
    print(r)


