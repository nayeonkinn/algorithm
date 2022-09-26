class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        def dfs(i):
            if i in trace:
                return False
            if i in visited:
                return True

            trace.add(i)
            for w in pre[i]:
                if not dfs(w):
                    return False
            trace.remove(i)
            visited.add(i)

            return True
            
        pre = defaultdict(list)
        for after, before in prerequisites:
            pre[after].append(before)
        
        trace = set()
        visited = set()
        
        for i in list(pre):
            if not dfs(i):
                return False
        
        return True
    