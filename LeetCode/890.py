from collections import Counter
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        pc = sorted(list(Counter(pattern).values()))

        results = []
        for word in words:

            wc = sorted(list(Counter(word).values()))

            tdict = {}
            c = 0
            LP = len(pattern)
            LW = len(word)
            if LP != LW:
                continue
            else:
                for i in range(LP):
                    if pattern[i] not in tdict:
                        tdict.update({ pattern[i]: word[i]})
                        c = c + 1
                    elif pattern[i] in tdict:
                        if tdict[pattern[i]] == word[i]:
                            c = c + 1
            print(c)
            if c == LP and pc == wc:
                results.append(word)
        return results

if __name__ == "__main__":

    s = Solution()

    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"

    r = s.findAndReplacePattern(words, pattern)
    print(r)

