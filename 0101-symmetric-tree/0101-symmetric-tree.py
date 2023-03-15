# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def recur(node, other):
            
            #If both are not defined then it is symetrical
            if not node and not other:
                return True
            
            #if there is one but not the other then it is not symetrical
            if not node or not other:
                return False
            
            #if the values dont match it is not symetrical
            if node.val != other.val:
                return False
            
            return recur(node.left, other.right) and recur(node.right, other .left)
            
        return recur(root.left, root.right)