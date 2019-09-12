def outer():
    out = "This is outer function--"

    def inner():
        print(out)
    return inner

if __name__ == "__main__":

    ref = outer()
    ref()