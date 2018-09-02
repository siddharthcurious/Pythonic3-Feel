class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        successprs  = sentence.split()
        rsmap = {}
        for root in dict:
            r = []
            for word in successprs:
                if root in word:
                    r.append(word)
            rsmap.update({root: sorted(r, key=lambda x:len(x))})




if __name__ == "__main__":

    s = Solution()

    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the batteryy battery"
    s.replaceWords(dict, sentence)

