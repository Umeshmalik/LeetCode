from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        G = defaultdict(list)
        for v,w,cost in roads:
            G[v].append((w,cost))
            G[w].append((v,cost))
        visited = set()
        costs = set()
        def dfs(v):
            if v in visited: return
            visited.add(v)
            for w, cost in G[v]:
                costs.add(cost)
                dfs(w)
        dfs(1)
        return min(costs)