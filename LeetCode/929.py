from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        remails = set()
        for email in emails:

            em = email.split("@")
            em[0] = em[0].replace(".", "")
            rname = em[0].split("+")[0]
            newemail = rname+"@"+em[1]
            remails.add(newemail)
        return len(remails)

if __name__ == "__main__":

    obj = Solution()
    i = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    r  = obj.numUniqueEmails(i)
    print(r)