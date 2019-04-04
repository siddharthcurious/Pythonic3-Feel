class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        L = len(chars)
        if L == 1:
            return chars
        i = 0
        c = 1
        track = 0
        while i < L - 1:
            if chars[i] == chars[i+1]:
                c += 1
            else:
                if c > 1:
                    num = str(c)
                    chars[track] = chars[i]
                    track += 1
                    for n in num:
                        chars[track] = n
                        track += 1
                else:
                    chars[track] = chars[i]
                    track += 1
                c = 1
            i += 1
        chars[track] = chars[i]
        track += 1
        if c > 1:
            for n in str(c):
                chars[track] = n
                track += 1

        return track

if __name__ == "__main__":

    obj = Solution()
    chars = ["a","a","b","b","c","c","c","d","e","e","e","f","f"]
    chars = ["a", "c", "c", "c", "c", "c", "c", "d"]
    chars = ["a", "c", "c", "c","d", "e", "e"]
    chars = ["a", "b"]
    r = obj.compress(chars)
    print(r)
