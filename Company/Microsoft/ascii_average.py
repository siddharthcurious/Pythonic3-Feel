string = "hello"
L = len(string)

S = 0
for c in string:
    S = S + ord(c)

print(S/L)