from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r, c = len(board), len(board[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs_find(i, j):
            if 0 <= i < r and 0 <= j < c and board[i][j] == 'O':
                board[i][j] = 'T'
                for d in directions:
                    dfs_find(i+d[0], j+d[1])

        for i in range(r):
            for j in range(c):
                if (i == 0 or i == r-1 or j == 0 or j == c-1) and board[i][j] == 'O':
                    dfs_find(i, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s = Solution()
    s.solve(board)
    print(board)
