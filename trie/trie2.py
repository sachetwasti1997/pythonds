class WordDictionary:

    def __init__(self):
        self.map = {}
        self.isEnd = False

    def addWord(self, word: str) -> None:
        temp = self
        for i in word:
            if i not in temp.map:
                temp.map[i] = WordDictionary()
            temp = temp.map[i]
        temp.isEnd = True

    def search(self, word: str) -> bool:
        def findRec(i, temp):
            if i == len(word):
                return temp.isEnd
            if word[i] != '.':
                if word[i] not in temp:
                    return False
                else:
                    temp = temp.map[word[i]]
                    return findRec(i+1, temp)
            else:
                b = False
                for word[i] in temp.map:
                    b = b or findRec(i+1, temp.map[word[i]])
                return b

        return findRec(0, self)

if __name__ == '__main__':
    pass
