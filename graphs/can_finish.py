def canFinish(self, numCourses: int, prerequisites) -> bool:
    graph, visited, isBeingVisited = {i:[] for i in range(numCourses)}, set(), set()

    for i in prerequisites:
        graph[i[0]].append(i[1])

    def dfs_Find(node: int):
        visited.add(node)
        isBeingVisited.add(node)
        for k in graph[node]:
            if k not in visited and dfs_Find(k):
                return True
            elif k in isBeingVisited:
                return True
        isBeingVisited.remove(node)
        return False

    for i in graph:
        if i not in visited:
            if dfs_Find(i): return False

    return True
