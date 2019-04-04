import operator
def maximize(tb):
    select = {}
    price = 0
    tbs = sorted(tb, key=operator.itemgetter(0), reverse=True)
    for k, v in tbs:
        if select.get(v) == None:
            price += k
            select.update({v: k})
    return price

if __name__ == "__main__":

    n, m = map(lambda x:int(x), input().split())

    tb = []
    for _ in range(n):
        t, b = map(lambda x:int(x), input().split())
        tb.append((t, b))

    r = maximize(tb)
    print(r)