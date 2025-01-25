# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list starting from the dummy node
        while current.next:
            if current.next.val == val:
                # Skip the node with the value 'val'
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the new head (dummy.next points to the modified head)
        return dummy.next