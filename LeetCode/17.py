from itertools import combinations
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits ==  "":
            return []

        num_alpha_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        if len(digits) == 1:
            return list(num_alpha_map[digits[0]])

        L = len(digits)
        combstr = ""
        for d in digits:
            combstr += num_alpha_map[d]
        combi = combinations(combstr, L)

        r = ["".join(c) for c in combi]
        return list(set(r))


if __name__ == "__main__":

    s = Solution()
    digits = "234"
    r = s.letterCombinations(digits)
    print(r)
    print(len(r))

    # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    # ['ab', 'ac', 'ad', 'ae', 'af', 'bc', 'bd', 'be', 'bf', 'cd', 'ce', 'cf', 'de', 'df', 'ef']
    # ['cf', 'bf', 'ad', 'be', 'af', 'bd', 'ce', 'cd', 'ae']
    # ['af', 'ce', 'ac', 'cf', 'ef', 'ad', 'ab', 'de', 'df', 'ae', 'bc', 'cd', 'bd', 'bf', 'be']
    # ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]
    # ['bb', 'ac', 'bc', 'cb', 'aa', 'ca', 'cc', 'ba', 'ab']

