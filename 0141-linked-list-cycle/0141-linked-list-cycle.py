# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
            
            nodes = {}
            node = head
            
            while node:
                
                if node not in nodes:
                    nodes[node] = node.val
                    node = node.next
                    
                else:
                    return True
                
            return False