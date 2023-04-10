# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        
        self.ans = []
        
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def helper(node):
            
            if node is None:
                return
            
            self.ans.append(node.val)
            helper(node.left)
            helper(node.right)
            
            return self.ans
        
        return helper(root)
            
                