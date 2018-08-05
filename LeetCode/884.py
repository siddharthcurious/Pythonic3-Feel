class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K == 1:
            return S[0]

        decoded = ""
        flag = False

        for e in S:
            if e >= "a" and e <= "z":
                decoded = decoded + e
            else:
                times = int(e)
                d = decoded
                decoded = d * times
                if len(decoded) >= K:
                    return decoded[K-1]
        if flag == False:
            return decoded[K-1]

if __name__ == "__main__":

    s = Solution()
    S = "leet2code3"
    K = 10
    S = "ha22"
    K = 5
    S = "a23699"
    K = 1
    S = "y959q969u3hb22odq595"
    K = 222280369
    ind = s.decodeAtIndex(S, K)
    print(ind)
