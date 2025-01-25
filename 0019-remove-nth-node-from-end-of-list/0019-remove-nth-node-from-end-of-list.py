# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Step 1: Move first pointer n steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Step 2: Move both first and second pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Step 3: Remove the nth node from the end
        second.next = second.next.next
        
        # Return the head of the modified list (skip the dummy node)
        return dummy.next