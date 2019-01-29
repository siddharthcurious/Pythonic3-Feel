def possible_words(num):

    mapped = {
        "1": "",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
        "0": ""
    }

    for e in num:
        val = mapped[e]
        for letter in val:
            print(letter)

if __name__ == "__main__":

    num = "456"
    r = possible_words(num)
    print(r)