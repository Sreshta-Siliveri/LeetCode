# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        # Traverse through the list
        while current is not None and current.next is not None:
            # If current node's value is the same as the next node's value
            if current.val == current.next.val:
                # Skip the next node by pointing to the next of the next node
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        
        return head
