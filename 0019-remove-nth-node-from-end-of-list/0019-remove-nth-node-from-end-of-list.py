# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize the pointers
        slow = fast = dummy
        
        # Move the fast pointer n steps ahead
        for i in range(n):
            fast = fast.next
        
        # Move both pointers until the fast pointer reaches the end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node by bypassing it
        slow.next = slow.next.next
        
        # Return the head of the list
        return dummy.next
                
            
        
            
            