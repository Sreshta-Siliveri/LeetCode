# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        
        # Step 1: Find the middle of the list using the slow and fast pointer approach
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list into two halves
        second_half = slow.next
        slow.next = None  # Split the list into two parts
        
        # Step 3: Reverse the second half
        prev, curr = None, second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_half = prev  # Now `second_half` is the reversed second half
        
        # Step 4: Merge the two halves
        first_half = head
        while second_half:
            # Save the next nodes
            tmp1, tmp2 = first_half.next, second_half.next
            
            # Rearranging the nodes
            first_half.next = second_half
            second_half.next = tmp1
            
            # Move the pointers forward
            first_half = tmp1
            second_half = tmp2