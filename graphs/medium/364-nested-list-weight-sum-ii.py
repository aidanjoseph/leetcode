'''
Literally same as the first one
just two passes
can do in a single pass but time complexity same
although single pass is cleaner
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        maxDepth = [1]
        def dfs(nest, depth):
            if isinstance(nest, NestedInteger) and nest.isInteger():
                return nest.getInteger() * depth
            sum = 0 
            maxDepth[0] = max(maxDepth[0], depth)
            weight = maxDepth[0] - depth + 1
            for i in range(len(nest)):
                if nest[i].isInteger():
                    sum += nest[i].getInteger() * weight
                else:
                    sum += dfs(nest[i].getList(), depth + 1)
            return sum 
        dfs(nestedList, 1)
        return dfs(nestedList, 1)
        