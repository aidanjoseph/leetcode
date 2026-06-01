'''
pretty simple
precuror to 1382, although i thought the inorder traversal part was easier than this part
but now we understand, can employ algos like binary search etc in tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(begin, end):
            if begin > end:
                return
            mid = begin + (end - begin) // 2
            left = create(begin, mid - 1)
            right = create(mid + 1, end)
            node = TreeNode(nums[mid], left, right)
            return node
        return create(0, len(nums) - 1)
        
