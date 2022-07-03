from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        graph = {i: [] for i in range(numCourses)}

        for i in prerequisites:
            if i[0] not in graph:
                graph[i[0]] = []
            graph[i[0]].append(i[1])

        res, visited, being_visited = [], set(), set()

        def has_cycle(node: int) -> bool:
            visited.add(node)
            being_visited.add(node)
            for i in graph[node]:
                if i not in visited and has_cycle(i):
                    return True
                elif i in being_visited:
                    return True
            res.append(node)
            being_visited.remove(node)
            return False

        for i in graph:
            if i not in visited and has_cycle(i):
                return []

        return res

if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    s = Solution()
    r = s.findOrder(numCourses, prerequisites)
    print(r)
