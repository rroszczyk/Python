class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

def main():
    keys = ["ala", "alabaster", "alabastrowe", "abrewacja", "absencja",
            "bajka", "bajkopis", "bajkowy", "bajkopisarz"]
    output = ["nie ma w drzewie",
              "jest w drzewie"]

    t = Trie()

    for key in keys:
        t.insert(key)

    print("{} ---- {}".format("ala", output[t.search("ala")]))
    print("{} ---- {}".format("alabaster", output[t.search("alabaster")]))
    print("{} ---- {}".format("aleopatia", output[t.search("aleopatia")]))
    print("{} ---- {}".format("bajka", output[t.search("bajka")]))


if __name__ == '__main__':
    main()

