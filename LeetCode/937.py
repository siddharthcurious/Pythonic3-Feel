from typing import List

import operator
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter_logs = []
        digits_logs = []

        for log in logs:
            log_decode = log.split()
            if log_decode[1][0] >= "0" and log_decode[1][0] <= "9":
                digits_logs.append(log)
            else:
                letter_logs.append(log.split(" ", 1))
        #print(digits_logs)

        logs = []

        lg = sorted(letter_logs, key=operator.itemgetter(1))

        for log in lg:
            logs.append(" ".join(log))

        for log in digits_logs:
            logs.append(log)

        return logs



if __name__ == "__main__":

    obj = Solution()
    i = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    i = ["n 1 6", "r wyv", "7 72", "4 95", "x 706"]

    r = obj.reorderLogFiles(i)
    print(r)

