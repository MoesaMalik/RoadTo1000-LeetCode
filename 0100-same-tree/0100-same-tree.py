# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
            def recur(node, other):
                
                if not node and not other:
                    return True
                
                if not node or not other:
                    return False
                
                if node.val != other.val:
                    return False
                
                return recur(node.left, other.left) and recur(node.right, other.right)
            
            return recur(p, q)