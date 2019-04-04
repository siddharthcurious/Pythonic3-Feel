class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cmap = {}
        for domain in cpdomains:
            count, dom = domain.split()
            count = int(count)
            doms = dom.split(".")
            L = len(doms)
            k = L - 1

            if cmap.get(doms[k]):
                c = cmap.get(doms[k])
                newc = c + count
                cmap[doms[k]] = newc
            else:
                cmap[doms[k]] = count

            if cmap.get(doms[k-1]+"."+doms[k]):
                c = cmap.get(doms[k-1]+"."+doms[k])
                newc = c + count
                cmap[doms[k-1]+"."+doms[k]] = newc
            else:
                cmap[doms[k-1] + "." + doms[k]] = count

            if len(doms) > 2:
                if cmap.get(dom):
                    c = cmap.get(dom)
                    newc = c + count
                    cmap[dom] = newc
                else:
                    cmap[dom] = count
        result = []
        for key, value in cmap.items():
            result.append(str(value)+" "+key)
        return result

if __name__ == "__main__":

    s = Solution()
    d = ["9001 discuss.leetcode.com"]
    d = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    r = s.subdomainVisits(d)
    print(r)