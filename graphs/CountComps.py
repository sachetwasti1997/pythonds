def validTree(n: int, edges) -> bool:
    if n == 1: return True
    parent = [i for i in range(n)]
    rank = [1 for i in range(n)]
    count = n

    def find(node: int) -> int:
        if node != parent[node]:
            parent[node] = find(parent[node])
        return parent[node]

    def union(i: int, j: int) -> bool:
        par1 = find(i)
        par2 = find(j)
        if par1 == par2:
            return False
        if rank[par1] > rank[par2]:
            parent[par2] = par1
        elif rank[par1] < rank[par2]:
            parent[par1] = par2
        else:
            parent[par2] = par1
            rank[par1] += 1
        return True

    for i in edges:
        if not union(i[0], i[1]):
            return False
        count -= 1

    return count == 1


class Solution:
    pass
