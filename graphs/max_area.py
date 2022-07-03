from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    r, c = len(grid), len(grid[0])
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def find_dfs(i: int, j: int) -> int:
        if 0 <= i < r and 0 <= j < c and grid[i][j] == 1:
            res = 1
            grid[i][j] = 0
            for d in directions:
                res += find_dfs(i+d[0], j+d[0])
            return res
        return 0

    max_area = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                max_area = max(max_area, find_dfs(i, j))

    return max_area
