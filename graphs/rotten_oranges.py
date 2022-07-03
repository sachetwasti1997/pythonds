from typing import List
from collections import deque

def orangesRotting(grid: List[List[int]]) -> int:
    r, c, onecount = len(grid), len(grid[0]), 0
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = deque()
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                onecount += 1
    max_time = 0
    while len(q) != 0:
        t = q.popleft()
        for d in directions:
            row, col = t[0]+d[0], d[1]+t[1]
            if 0 <= row < r and 0 <= col < c and grid[row][col] == 1:
                grid[row][col] = 0
                time = t[2] + 1
                max_time = max(max_time, time)
                onecount -= 1
                q.append((row, col, time))
    return max_time if onecount == 0 else -1

if __name__ == '__main__':
    time = orangesRotting([[2,1,1],[1,1,0],[1,0,1]])
    print(time)
