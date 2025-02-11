# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = merged_list = ListNode()

        # traverse over linked list nodes while node1 is not None and while node2 is not None
        while list1 and list2:
            if list1.val < list2.val:
                merged_list.next = list1
                list1 = list1.next
                merged_list = merged_list.next
            else:
                merged_list.next = list2
                list2 = list2.next
                merged_list = merged_list.next
        merged_list.next = list1 if list1 else list2
        return merged_head.next

        # time complexity: O(max(n, m)) -> n is list1 len, m is list2 len
        # space complexity: O(1) -> excluding output linked list
