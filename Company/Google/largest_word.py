def isSubsequence(word, target):

    L1 = len(word)
    L2 = len(target)

    matrix = [ [0 for _ in range(L2+1)] for _ in range(L1+1)]

    for i in range(L1+1):
        for j in range(L2+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif word[i-1] == target[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    if matrix[L1][L2] == L1:
        return True

def longest_word(dict, target):
    l = 0
    w = ""
    for word in dict:
        if isSubsequence(word, target):
            if len(word) > l:
                l = len(word)
                w = word
    return w

if __name__ == "__main__":

    dict = ["ale", "apple", "monkey", "plea"]
    target = "abpcplea"
    r = longest_word(dict, target)
    print(r)
