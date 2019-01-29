def permute(input, prefix):
    if not input:
        print(prefix)
    else:
        for i in range(len(input)):
            permute(input[:i]+input[i+1:], prefix + [input[i]])

if __name__ == "__main__":

    input = ["S", "A", "N"]
    prefix = []
    permute(input, prefix)