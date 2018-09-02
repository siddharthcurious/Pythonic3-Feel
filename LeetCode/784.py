class Solution:
    def letterCasePermutation(self, S):
        self.out = []
        self.capitalizeAndJoin(S, '', 0)

        return self.out

    def capitalizeAndJoin(self, s, ans, index):
        if (index == len(s)):
            self.out.append(ans)
            return
        i = index
        while (i < len(s)):
            if s[i].isnumeric():
                ans += s[i]
            else:
                self.capitalizeAndJoin(s, ans + s[i].lower(), i + 1)
                self.capitalizeAndJoin(s, ans + s[i].upper(), i + 1)
                break
            i += 1

        if (i == len(s)):
            self.out.append(ans)


if __name__ == "__main__":

    s = Solution()

    S = "a1b2"

    r = s.letterCasePermutation(S)
    print(r)