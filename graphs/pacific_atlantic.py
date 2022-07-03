from typing import List

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    r, c = len(heights), len(heights[0])
    directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

    def dfs_height_fill(i, j, prev, ocean):
        if 0 <= i < r and 0 <= j < c and heights[i][j] >= prev and not ocean[i][j]:
            ocean[i][j] = True
            for d in directions:
                dfs_height_fill(i+d[0], j+d[1], heights[i][j], ocean)

    pacific, atlantic = [[False] * c for i in range(r)], [[False] * c for _ in range(r)]
    for i in range(r):
        dfs_height_fill(i, 0, -1, pacific)
        dfs_height_fill(i, c - 1, -1, atlantic)
    for i in range(c):
        dfs_height_fill(0, i, -1, pacific)
        dfs_height_fill(r-1, i, -1, atlantic)
    print(pacific)
    print(atlantic)
    resList = []
    for i in range(r):
        for j in range(c):
            if pacific[i][j] and atlantic[i][j]:
                resList.append([i, j])

    return resList

if __name__ == '__main__':
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    t = pacificAtlantic(heights)
    print(t)
    # pacific, atlantic = [[0] * 3] * 3, [[0] * 3] * 3
    # print(pacific)
    # pacific[0][0] = 100
    # print(pacific)
