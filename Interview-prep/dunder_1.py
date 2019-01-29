class Numbers:

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def add(self):
        return self.a + self.b

    def __repr__(self):
        return "Add numbers __repr__"

    def __str__(self):
        return "Add numbers __str__"


if __name__ == "__main__":

    s = Numbers(10, 20)
    print(s)
    print(repr(s))
    print(str(s))
