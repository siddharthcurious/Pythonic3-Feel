def permute(string, choosen):
    if len(choosen) == len(string):
        print(choosen)
    else:
        for c in string:
            choosen.append(c)
            permute(string, choosen)
            choosen.pop()

if __name__ == "__main__":

    permute("SAND", [])