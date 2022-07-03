from typing import List


class Trie:
    def __init__(self):
        self.map = {}
        self.word = ''
        self.isEnd = False

    def insert(self, word):
        temp = self
        for i in word:
            if i not in temp.map:
                temp.map[i] = Trie()
            temp = temp.map[i]
        temp.word = word
        temp.isEnd = True


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    r, c = len(board), len(board[0])
    direc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    resList, visit = set(), set()

    def dfs_find(i, j, root):
        if root.isEnd:
            resList.add(root.word)
        if i < 0 or i >= r or j < 0 or j >= c or (i,j) in visit or board[i][j] not in root.map:
            return
        temp = board[i][j]
        visit.add((i,j))
        for d in direc:
            dfs_find(i + d[0], j + d[1], root.map[temp])
        visit.remove((i,j))

    root = Trie()

    for m in words:
        root.insert(m)

    for k in range(r):
        for l in range(c):
            dfs_find(k, l, root)

    return list(resList)


if __name__ == '__main__':
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(findWords(board, words))
