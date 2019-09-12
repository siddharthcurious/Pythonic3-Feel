from collections import defaultdict
def get_subsequence(pattern):

    d = defaultdict(list)
    for i in range(0, len(pattern)):
        j = i + 1
        while j <= len(pattern):
            sub = pattern[i:j]
            d[len(sub)].append(sub)
            j += 1
    # print(d)

    for key, value in d.items():
        print("{}:{}".format(key, value))

if __name__ == "__main__":

    get_subsequence("helloworld")