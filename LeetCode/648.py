class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words  = sentence.split()
        L = len(words)
        for root in dict:
            i = 0
            l = len(root)
            print(root)
            while i < L:
                if len(words[i]) > l and words[i][0:l] == root:
                    words[i] = root
                i += 1
        return " ".join(words)

if __name__ == "__main__":

    s = Solution()

    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the batteryy"
    r = s.replaceWords(dict, sentence)
    print(r)

