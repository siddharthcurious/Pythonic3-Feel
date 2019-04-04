from collections import defaultdict
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wordsmap = defaultdict(list)
        for word in words:
            l = len(word)
            wordsmap[l].append(word)

        L = len(wordsmap)
        for i in range(1, L+1):
            pass



if __name__ == "__main__":

    s = Solution()
    words = ["w", "wo", "wor", "worl", "world", "worle"]
    r = s.longestWord(words)
    print(r)