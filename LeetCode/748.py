from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        result = ""
        lp = licensePlate.lower()
        lp_count = Counter(lp)
        new_lp = { k:v for k, v in lp_count.items() if k >= 'a' and k <= 'z'}

        for word in words:
            word_counter = Counter(word)
            w = True
            for k, v in new_lp.items():
                if k not in word_counter.keys():
                    w = False
                    break
                elif word_counter[k] < v:
                    w = False
                    break

            if w == True:
                if result == "":
                    result = word
                elif len(result) > len(word):
                    result = word
        return result

if __name__ == "__main__":

    s = Solution()
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]

    licensePlate = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    r = s.shortestCompletingWord(licensePlate, words)
    print(r)
