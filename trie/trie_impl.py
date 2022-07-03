class Trie:

    def __init__(self):
        self.map = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        temp = self
        for i in word:
            if i not in temp.map:
                temp.map[i] = Trie()
            temp = temp.map[i]

        temp.isEnd = True

    def search(self, word: str) -> bool:
        temp, i = self, 0
        while i < len(word):
            if word[i] not in temp.map:
                return False
            temp = temp.map[word[i]]
            i += 1
        return temp.isEnd

    def startsWith(self, prefix: str) -> bool:
        temp, i = self, 0
        while i < len(prefix):
            if prefix[i] not in temp.map:
                return False
            temp = temp.map[prefix[i]]
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie)

