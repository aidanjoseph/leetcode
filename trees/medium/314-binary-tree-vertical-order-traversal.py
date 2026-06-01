'''
seen before
nice pattern
use of defaultdict better from last time
also better to just add val directly 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        left = 0
        right = 0
        q = collections.deque([])
        nums = defaultdict(list)
        q.append((root, 0))
        while q:
            for _ in range(len(q)):
                node, pos = q.popleft()
                left = min(left, pos)
                right = max(right, pos)
                nums[pos].append(node.val)
                if node.left:
                    q.append((node.left, pos - 1))
                if node.right:
                    q.append((node.right, pos + 1))
        res = []
        for i in range(left, right+1):
            res.append(nums[i])
        return res

    
