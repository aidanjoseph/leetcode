'''
ts kinda hard, had to look at prev solution
makes senese
first intuition was a bfs, but realizedi a lot of recursive work and then dfs
would talk out loud for interview but don't do as much in practice I suppose s
'''



"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #sounds like bfs?
        #just bfs from original, keep seen set, seen is just the val number i suppose
        
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
            
                
        