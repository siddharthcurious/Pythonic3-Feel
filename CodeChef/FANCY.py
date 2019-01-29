def quotes(quote):
    q = quote.split()
    if "not" in q:
        return "Real Fancy"
    else:
        return "regularly fancy"

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        q = input()
        r = quotes(q)
        print(r)