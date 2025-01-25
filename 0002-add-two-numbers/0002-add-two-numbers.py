# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0  # Initialize carry to 0
        
        # Traverse both linked lists until both are None
        while l1 or l2 or carry:
            # Get the values from l1 and l2; if None, use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute the sum of the values and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Compute the new carry
            current.next = ListNode(total % 10)  # Add the digit to the result
            
            # Move to the next nodes
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example usage
solution = Solution()

# Example 1
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = solution.addTwoNumbers(l1, l2)
print("Output for Example 1:", end=" ")
print_linked_list(result)

# Example 2
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print("Output for Example 2:", end=" ")
print_linked_list(result)

# Example 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print("Output for Example 3:", end=" ")
print_linked_list(result)