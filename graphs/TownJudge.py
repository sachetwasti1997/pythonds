from typing import List


class EdgesCnt:
    def __init__(self):
        self.incom = 0
        self.outgo = 0


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        gr = {i: EdgesCnt() for i in range(1, n + 1)}
        for i in trust:
            gr[i[0]].outgo += 1
            gr[i[1]].incom += 1
        for i in gr.items():
            if i[1].outgo == 0 and i[1].incom == n - 1:
                return i[0]
        return -1
