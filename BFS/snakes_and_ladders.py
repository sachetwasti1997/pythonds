from typing import List


class Solution:
  def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)
    i = 1
    bgr = {}
    for i in range(n - 1, -1, -1):
      for j in board[i]:
        bgr[i] = j
        i += 1
    visit = set()
    visit.add(1)
    q = [i]
    stps = 0
    while not len(q) == 0:
      tmp = q.pop()
      flag = -1
      if tmp == n * n:
        break
      stps += 1
      for i in range(tmp + 1, min(tmp + 6, n * n)):
        if i not in visit:
          if bgr[i] != -1:
            flag = 1
            q.append(bgr[i])
        visit.add(i)
      if flag == -1:
        q.append(tmp + 6)
    return stps
