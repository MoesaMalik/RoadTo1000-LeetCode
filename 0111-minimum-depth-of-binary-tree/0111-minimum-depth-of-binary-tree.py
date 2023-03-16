# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        self.minD = float('inf')
        self.recur(root, 0)
        return self.minD
        
    def recur(self, node, cur_depth):
        
        if not node:
            return 
        
        #leaf node
        if not node.left and not node.right:
            
            self.minD = min(self.minD, cur_depth + 1)
        self.recur(node.left, cur_depth + 1)
        self.recur(node.right, cur_depth + 1)
            
        
        
                
                
                
                
            