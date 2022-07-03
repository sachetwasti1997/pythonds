from collections import defaultdict
from typing import List


def alienOrder(words: List[str]) -> str:
    charm = {c: [] for w in words for c in w}

    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        for j in range(len(w1)):
            if j == len(w2): return ""
            if j < len(w2) and w1[j] != w2[j]:
                charm[w1[j]].append(w2[j])
                break

    visited = set()
    is_current = set()
    res = []

    def dfs(c) -> bool:
        visited.add(c)
        is_current.add(c)
        for k in charm[c]:
            if k not in visited and dfs(k):
                return True
            elif k in is_current:
                return True
        is_current.remove(c)
        res.append(c)
        return False

    for ch in charm:
        if ch not in visited and dfs(ch):
            return ""

    return "".join(res[::-1])

if __name__ == '__main__':
    t = alienOrder(["z","x","z"])
    #"wrt", "wrf", "er", "ett", "rftt"
    print(t)
