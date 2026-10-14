# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        max_dist = [0]
        def dfs(root, start):
            depth = 0
            if root is None:
                return depth
            left = dfs(root.left, start)
            right = dfs(root.right, start)
            if root.val == start:
                max_dist[0] = max(left, right)
                depth = -1
            elif left >= 0 and right >= 0:
                depth = max(left, right) + 1
            else:
                dist = abs(left) + abs(right)
                max_dist[0] = max(max_dist[0], dist)
                depth = min(left, right) - 1
            return depth
        dfs(root, start)
        return max_dist[0]