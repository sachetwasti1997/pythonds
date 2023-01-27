import sys
from queue import PriorityQueue
from typing import List
class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    p = PriorityQueue()
    CONST = 1000001
    p.put((0, src, 0))
    disArr = [CONST for i in range(0, n+1)]
    disArr[src] = 0
    gr = {i: [] for i in range(0, n)}
    for i in flights:
      gr[i[0]].append((i[1], i[2]))
    res = sys.maxsize
    while not p.empty():
      (dis, src, kv) = p.get()
      if src == dst and res > dis:
        res = dis
      if kv <= k:
        for i in gr[src]:
          if dis + i[1] < disArr[i[0]]:
            disArr[i[0]] = dis + i[1]
            p.put((disArr[i[0]], i[0], kv+1))
    return res

if __name__ == '__main__':
  s = Solution()
  s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
