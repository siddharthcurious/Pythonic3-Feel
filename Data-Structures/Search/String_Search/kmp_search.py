class KMP_Search:

    def __get_pie_table(self, pattern):
        L = len(pattern)
        pie = [0] * L

        k = 0
        i = 1

        while i < L:
            if(pattern[i] == pattern[k]):
                pie[i] = pie[i-1] + 1
                i += 1
                k += 1
            else:
                pie[i] = 0
                i += 1
                k = 0

        return pie

    def kmp_search(self, pattern, text):

        pie_table = self.__get_pie_table(pattern)

        i = 0
        j = 0
        L = len(text)
        print(pie_table)
        while i < L:
            if(text[i] == pattern[j]):
                if(j == len(pattern)-1):
                    print(i, j)
                    return True
                i += 1
                j += 1
                continue
            else:
                if j == 0:
                    i += 1
                else:
                    j = pie_table[j]
        return False

if __name__ == "__main__":

    obj = KMP_Search()
    r = obj.kmp_search("ababd", "abaccababd")
    print(r)
