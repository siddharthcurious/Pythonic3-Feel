from operator import itemgetter

d = {
    1: "SAN",
    2: "JAN",
    3: "FEB",
    6: "MAR",
    5: "JUL",
    4: "AUG"
}

d1 = sorted(d.items(), key=itemgetter(0))

print(d1)
