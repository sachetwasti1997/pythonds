from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True
        graphs = {i: [] for i in range(numCourses)}
        visited, being_visited = set(), set()

        for i in prerequisites:
            graphs[i[0]].append(i[1])

        def find_cycle(node: int):
            visited.add(node)
            being_visited.add(node)
            for i in graphs[node]:
                if i not in visited and find_cycle(i):
                    return True
                elif i in being_visited:
                    return True
            being_visited.remove(node)
            return False

        for i in graphs:
            if i not in visited and find_cycle(i):
                return False

        return True
