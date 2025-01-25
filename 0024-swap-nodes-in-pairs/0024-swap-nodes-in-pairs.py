class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Dummy node to simplify handling the head node
        dummy = ListNode(-1)
        dummy.next = head
        
        prev = dummy  # prev will track the node before the pair we're swapping
        
        # Traverse the list, two nodes at a time
        while head and head.next:
            # Identify the two nodes to swap
            first = head
            second = head.next
            
            # Swap the nodes
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev and head for the next pair
            prev = first
            head = first.next
        
        return dummy.next
