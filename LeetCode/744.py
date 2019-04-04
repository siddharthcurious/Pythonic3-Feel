class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        L = len(letters)
        for i in range(L):
            if letters[i] > target:
                return letters[i]
        return letters[0]

if __name__ == "__main__":

    obj = Solution()
    letters = ["c", "f", "j"]
    target = "a"

    letters = ["c", "f", "j"]
    target = "g"
    r  = obj.nextGreatestLetter(letters, target)
    print(r)