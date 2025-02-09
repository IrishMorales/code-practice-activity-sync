# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = current_node = ListNode()
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            current_sum = digit1 + digit2 + carry

            carry = current_sum // 10
            next_node = ListNode(current_sum % 10)
            current_node.next = next_node
            current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head_node.next
        # time complexity: O(max(n, m)) -> n is length of l1, m is length of l2
        # space complexity: O(1) for processing, O(max(n, m) + 1) for answer
