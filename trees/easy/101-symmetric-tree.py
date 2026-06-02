'''
pretty chill, kinda had to do 100 and 226 before
but lowkey just think about it a little in terms of base cases
same as same tree, but just swap left and right
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameInverse(p, q):
            if p and not q:
                return False
            if q and not p:
                return False
            if not p and not q:
                return True
            if p.val == q.val:
                return isSameInverse(p.left, q.right) and isSameInverse(p.right, q.left)
            else:
                return False
        return isSameInverse(root.left, root.right)

        

        