from collections import Counter
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = ""
        count = Counter(T)
        print(count)
        for ch in S:
            if ch in count:
                cnt = count[ch]
                for _ in range(cnt):
                    result += ch
                count.pop(ch)

        for ch in T:
            if ch in count:
                cnt = count[ch]
                for _ in range(cnt):
                    result += ch
                count.pop(ch)
        return result

if __name__ == "__main__":

    s = Solution()
    S = "cbafg"
    T = "abcd"
    r = s.customSortString(S, T)
    print(r)

    S = "hucw"
    T = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
    r = s.customSortString(S, T)
    print(r)
