def main():
    T = int(input())
    for _ in range(T):
        string = input()
        out = ""
        for e in string:
            out += str(ord(e))
        print(out)
main()

