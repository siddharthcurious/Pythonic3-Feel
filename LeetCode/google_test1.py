from typing import List

class Solution:
    def __parseEmail(self, email):
        em = email.split("@")
        name = em[0]
        domain = em[1]
        name1 = name.split("+")[0]
        name2 = name1.split(".")
        name3 = "".join(name2)
        return name3+"@"+domain

    def numUniqueEmails(self, emails: List[str]) -> int:
        rset = set()
        for e in emails:
            rset.add(self.__parseEmail(e))
        return len(rset)

if __name__ == "__main__":

    obj = Solution()
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails = ["..+a.+a@b.b"]
    r = obj.numUniqueEmails(emails)
    print(r)
