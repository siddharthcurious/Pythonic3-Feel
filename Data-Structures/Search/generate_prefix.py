def get_prefix(pattern):
    c = 0
    for i in range(1, len(pattern)+1):
        c += 1
        print(pattern[:i])

    print(c)


get_prefix("ab")