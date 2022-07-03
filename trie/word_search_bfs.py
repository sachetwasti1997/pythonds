from collections import deque
from typing import List
import copy

class Trie:
    def __init__(self):
        self.map = {}
        self.word = ' '
        self.is_end = False

    def insert(self, word):
        temp = self
        for i in word:
            if i not in temp.map:
                temp.map[i] = Trie()
            temp = temp.map[i]
        temp.is_end = True
        temp.word = word


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    r, c = len(board), len(board[0])
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    resList = set()

    def bfs_find(i, j, root):
        d = deque()
        d.append((i, j))
        visit = set()
        if root.is_end: resList.add(board[i][j])
        root = root.map[board[i][j]]
        while len(d) > 0:
            t = d.popleft()
            if root.is_end:
                resList.add(root.word)
            visit.add((t[0], t[1]))
            for dir in directions:
                row, col = t[0] + dir[0], t[1] + dir[1]
                if 0 <= row < r and 0 <= col < c and (row, col) not in visit and board[row][col] in root.map:
                    d.append((row, col))
                    root = root.map[board[row][col]]

    root = Trie()
    for i in words:
        root.insert(i)

    for i in range(r):
        for j in range(c):
            if board[i][j] in root.map: bfs_find(i, j, root)

    return list(resList)

if __name__ == '__main__':
    t = findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
              ["oath","pea","eat","rain"])
    print(t)
