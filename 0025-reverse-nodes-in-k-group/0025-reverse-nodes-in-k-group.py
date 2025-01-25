# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        # Function to reverse a linked list in place
        def reverse_linked_list(head, k):
            prev, curr = None, head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        
        # Dummy node to simplify edge case handling
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy  # This will point to the node before each group

        # Count the total number of nodes in the list
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        # Reverse nodes in groups of k
        while count >= k:
            group_head = group_prev.next
            group_tail = group_head
            # Find the tail of the group
            for i in range(k - 1):
                group_tail = group_tail.next
            
            # Save the next node to connect later
            next_group = group_tail.next
            
            # Reverse the group
            group_tail.next = None  # Break the link to the rest of the list
            group_prev.next = reverse_linked_list(group_head, k)
            
            # Now group_head is the tail of the reversed group
            group_head.next = next_group
            group_prev = group_head  # Move group_prev to the end of the reversed group
            
            count -= k  # Decrease count by k for each group reversed
        
        return dummy.next