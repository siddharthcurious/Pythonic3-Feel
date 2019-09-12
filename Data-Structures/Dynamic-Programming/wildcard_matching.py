def isMatch(string, pattern):
    if string == pattern:
        return True
    elif string == "" and pattern == "*":
        return True
    elif pattern == "" or string == "":
        return False
    elif string[0] == pattern[0]:
        return isMatch(string[1:], pattern[1:])
    elif pattern[0] == "?":
        return isMatch(string[1:], pattern[1:])
    elif pattern[0] == "*":
        return isMatch(string, pattern[1:]) or isMatch(string[1:], pattern)
    elif string[0] != pattern[0]:
        return False

if __name__ == "__main__":

    string = "abc"
    pattern = "*a*c"
    r = isMatch(string, pattern)
    print(r)