class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class ImplementTrie(object):
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def search(self, key):
        pass

    def insert(self, key):
        pcrawl = self.root
        for ch in key:
            ind = self.get_index(ch)
            if not pcrawl.children[ind]:
                pcrawl.children[ind] = True
                pass

if __name__ == "__main__":

    obj = ImplementTrie()
    obj.insert("sand")