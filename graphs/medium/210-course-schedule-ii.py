class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = []
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj[pre[1]].append(pre[0])

        q = collections.deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            top = q.popleft()
            res.append(top)
            for next_node in adj[top]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        if len(res) != numCourses:
            return []
        return res
        