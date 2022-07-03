from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def mark_cells(i, j, visit, prev):
            if 0 <= i < r and 0 <= j < c and prev <= heights[i][j] and (i, j) not in visit:
                visit.add((i, j))
                for d in direction:
                    mark_cells(i + d[0], j + d[1], visit, heights[i][j])

        for i in range(r):
            mark_cells(i, 0, pacific, -1)
            mark_cells(i, c-1, atlantic, -1)

        for i in range(c):
            mark_cells(0, i, pacific, -1)
            mark_cells(r-1, i, atlantic, -1)

        res = []
        for i in range(r):
            for j in range(c):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res

if __name__ == '__main__':
    s = Solution()
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    t = s.pacificAtlantic(heights)
    print(t)
