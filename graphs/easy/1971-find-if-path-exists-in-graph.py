'''
kinda hard
union find is a solution could learn

kinda suck at these adjancey list representations
chill with 2d graph representations but this kinda weird yeah 
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #use a set?
        #reachable from start -- starts trivially from source
        #keep adding as we see those reachable, if dest is in reachable from start
        #we return, assumes ordering
        #2 passes?
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = [False] * n
        def dfs(node):
            if node == destination:
                return True
            seen[node] = True
            for nextNode in graph[node]:
                if not seen[nextNode]:
                    if dfs(nextNode):
                        return True
            return False
        return dfs(source)
        