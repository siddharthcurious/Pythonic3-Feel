from typing import List

from collections import defaultdict
import os
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        dd = defaultdict(list)
        for data in paths:
            path = data.split()
            dir = path[0]
            files = path[1:]
            for file in files:
                fs  = file.split("(")
                filename = fs[0]
                content = fs[1][:-1]
                fullpath = os.path.join(dir, filename)
                dd[content].append(fullpath)

        result = []
        for key, value in dd.items():
            if len(value) > 1:
                result.append(value)
        return result


if __name__ == "__main__":

    obj = Solution()
    i = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    i = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
    r = obj.findDuplicate(i)
    print(r)