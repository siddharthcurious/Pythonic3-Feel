class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cont = {}
        for c in s:
            if c in cont:
                freq = cont[c]
                cont.update({c:freq+1})
            else:
                cont.update({c:1})
        cont_sorted = sorted(cont.items(), key=lambda x: x[1], reverse=True)
        result = ""
        for k, v in cont_sorted:
            while v:
                result += k
                v -= 1
        return result

if __name__ == "__main__":

    s = Solution()
    input = "tree"
    r = s.frequencySort(input)
    print(r)