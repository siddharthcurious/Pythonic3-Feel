class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        ordindex = {c: i for i, c in enumerate(order)}
        wlen = len(words)
        for i in range(wlen-1):
            word1 = words[i]
            word2 = words[i+1]

            minlen = min(len(word1), len(word2))

            for j in range(minlen):
                if word1[j] != word2[j]:
                    if ordindex.get(word1[j]) > ordindex.get(word2[j]):
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True

if __name__ == "__main__":

    obj = Solution()
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"

    r = obj.isAlienSorted(words, order)
    print(r)