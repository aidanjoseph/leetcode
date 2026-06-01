'''
kinda hard, did cheat
looked at solution
but understand
you get inorder traversal to make it easy
then you do a create thing, calculate mid index and stuff
kinda like a binary search type thing
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sortedList = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            sortedList.append(node.val)
            inOrder(node.right)
            return 
        def create(sorty, start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            left = create(sorty, start, mid - 1)
            right = create(sorty, mid + 1, end)
            node = TreeNode(sortedList[mid], left, right)
            return node
        inOrder(root)
        res = create(sortedList, 0, len(sortedList) - 1)
        return res
            

        