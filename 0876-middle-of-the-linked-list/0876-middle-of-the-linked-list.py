# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """two pointer method fast pointer and slow pointer the fast pointer will go double the speed of the slow pointer thus when we return the slow pointer it will be at the middle of the list"""
        
        fast = head
        slow = head
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
        
        return slow
        
        