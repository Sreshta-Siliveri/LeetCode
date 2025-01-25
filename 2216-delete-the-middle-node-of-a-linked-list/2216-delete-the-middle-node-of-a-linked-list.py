# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        # Initialize slow and fast pointers
        slow = head
        fast = head
        prev = None  # To keep track of the node before the middle node
        
        # Move fast pointer two steps at a time and slow pointer one step at a time
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # Delete the middle node by adjusting the next pointer of the previous node
        prev.next = slow.next
        
        return head