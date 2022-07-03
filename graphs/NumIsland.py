import array as List


class Solution:
    def numIslands(self, grid) -> int:
        dir1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = len(grid), len(grid[0])

        def dfs_find(k, l):
            if 0 <= k < r and 0 <= l < c and grid[k][l] == '1':
                grid[k][l] = '0'
                for d in dir1:
                    dfs_find(k + d[0], l + d[1])

        res = 0
        for i in range(0, r):
            for j in range(0, c):
                if grid[i][j] == '1':
                    res += 1
                    dfs_find(i, j)

        return res
