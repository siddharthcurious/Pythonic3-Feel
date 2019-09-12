class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        keyboard_list = list(keyboard)
        hashmap = {}
        for i, e in enumerate(keyboard_list):
            hashmap.update({e:i})

        prepos = 0
        steps = 0
        for ch in word:
            currentpos = hashmap.get(ch)
            steps += abs(currentpos - prepos)
            prepos = currentpos
        return steps

if __name__ == "__main__":

    obj = Solution()
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"

    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "p"
    r = obj.calculateTime(keyboard, word)
    print(r)