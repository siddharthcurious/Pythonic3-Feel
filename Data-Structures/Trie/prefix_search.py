class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = [None] * 26
        self.word_finished = False

def construct_trie(root, sentence, prefix):

    temp = root
    words = sentence.split()
    for word in words:
        for ch in word:
            index = ord(ch) - ord('a')
            if temp.children[index] == None:
                temp.children[index] = 1
                temp = temp
                pass





if __name__ == "__main__":

    prefix = "int"
    sentence = "this inter intermediate intersection all about knowledge integer and intersteller"

    root = TrieNode("*")
    r = prefix_match(root, sentence, prefix)
    print(r)
