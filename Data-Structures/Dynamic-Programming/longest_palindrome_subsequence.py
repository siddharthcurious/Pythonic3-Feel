def longest_palindrome_subsequence(string, i, j):
    if i == j:
        return 1
    if string[i] == string[j]:
        if j - i == 1:
            return 2
    if string[i] == string[j]:
        return 2 + longest_palindrome_subsequence(string, i+1, j-1)
    if string[i] != string[j]:
        return max(longest_palindrome_subsequence(string, i+1, j), longest_palindrome_subsequence(string, i, j-1))


if __name__ == "__main__":

    string = "dabbadf"
    L = len(string)
    r = longest_palindrome_subsequence(string, 0, L-1)
    print(r)