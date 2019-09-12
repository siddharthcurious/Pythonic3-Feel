# Python Implementation of the above approach

# Function to find the minimum number
# character change required
import math as ma


def change(s):
    # Finding the length of the string
    n = len(s)

    # To store the number of replacement operations
    cc = 0

    for i in range(n // 2):

        # If the characters at location
        # i and n-i-1 are same then
        # no change is required
        if (s[i] == s[n - i - 1]):
            continue

        # Counting one change operation
        cc += 1

        # Changing the character with higher
        # ascii value with lower ascii value
        if (s[i] < s[n - i - 1]):
            s[n - i - 1] = s[i]
        else:
            s[i] = s[n - i - 1]

    print("Minimum characters to be replaced = ", str(cc))
    print(*s, sep="")


# Driver code
s = "hunu"
change(list(s))
