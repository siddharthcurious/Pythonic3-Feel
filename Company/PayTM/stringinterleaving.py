# Python program to print all interleavings of given two strings

# Utility function
def toString(List):
	return "".join(List)

# The main function that recursively prints all interleavings.
# The variable iStr is used to store all interleavings (or output
# strings) one by one.
# i is used to pass next available place in iStr
def printIlsRecur(str1, str2, iStr, m, n, i):

	# Base case: If all characters of str1 and str2 have been
	# included in output string, then print the output string
	if m==0 and n==0:
		print(toString(iStr))

	# If some characters of str1 are left to be included, then
	# include the first character from the remaining characters
	# and recur for rest
	if m != 0:
		iStr[i] = str1[0]
		printIlsRecur(str1[1:], str2, iStr, m-1, n, i+1)

	# If some characters of str2 are left to be included, then
	# include the first character from the remaining characters
	# and recur for rest
	if n != 0:
		iStr[i] = str2[0]
		printIlsRecur(str1, str2[1:], iStr, m, n-1, i+1)

# Allocates memory for output string and uses printIlsRecur()
# for printing all interleavings
def printIls(str1, str2, m, n):
	iStr = [''] * (m+n)

	# print all interleavings using printIlsRecur()
	printIlsRecur(str1, str2, iStr, m, n, 0)

# Driver program to test the above function
str1 = "AB"
str2 = "CD"
printIls(str1, str2, len(str1), len(str2))

# This code is contributed by Bhavya Jain
