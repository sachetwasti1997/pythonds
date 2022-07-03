from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        row, col = len(rooms), len(rooms[0])
        q = deque()
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        while len(q) > 0:
            temp = q.popleft()
            for d in directions:
                r, c, dis = temp[0]+d[0], temp[1]+d[1], temp[2]
                if 0 <= r < row and 0 <= c < col and dis + 1 < rooms[r][c]:
                    q.append((r,c, dis+1))
                    rooms[r][c] = dis + 1

if __name__ == '__main__':
    rooms = [[-1]]
    s = Solution()
    s.wallsAndGates(rooms)
    print(rooms)