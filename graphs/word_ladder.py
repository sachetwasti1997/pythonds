from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}
        for i in wordList:
            for k in range(len(i)):
                key = i[0:k]+"*"+i[k+1:len(i)+1]
                if key not in graph:
                    graph[key] = []
                graph[key].append(i)
        q, visited, res = deque(), set(), 0
        q.append(beginWord)
        visited.add(beginWord)
        size = len(visited)
        while len(q) > 0:
            for l in range(size):
                t = q.popleft()
                if t == endWord: return res
                for k in range(len(t)):
                    key = t[0:k]+"*"+t[k+1:len(t)+1]
                    if key in graph:
                        for w in graph[key]:
                            if w in visited: continue
                            visited.add(w)
                            q.append(w)
                res += 1
                size = len(q)
        return res

if __name__ == '__main__':
    s = Solution()
    r = s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    print(r)