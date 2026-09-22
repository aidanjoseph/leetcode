class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        n = numCourses
        indegree = [0] * n
        q = collections.deque([])
        count = 0
        # adj = defaultdict(set)
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            indegree[pre[0]] += 1
            # adj[pre[1]].add(pre[0])
            adj[pre[1]].append(pre[0])
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            top = q.popleft()
            count += 1
            for next_node in adj[top]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        return count == n
