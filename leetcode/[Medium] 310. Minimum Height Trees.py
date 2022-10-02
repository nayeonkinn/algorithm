class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        if n == 1:
            return [0]

        adj = defaultdict(list)
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        leaves = []
        for i in list(adj):
            if len(adj[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            leaves2 = []
            
            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                
                if len(adj[neighbor]) == 1:
                    leaves2.append(neighbor)
            
            leaves = leaves2

        return leaves