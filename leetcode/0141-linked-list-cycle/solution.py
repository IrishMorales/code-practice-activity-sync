# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # brute force solution ---
        # loop over linked list while building a hashmap of the values and indices you've seen
        # if we see value + index that was already seen, return True
        # if loop ends, return False
        # time complexity: O(n)
        # space complexity: O(n)

        # two pointers ---
        # keep slow pointer and fast pointer
        slow_pointer = fast_pointer = head

        # loop over linked list while slow pointer != none and fast pointer != none
        while fast_pointer and fast_pointer.next and fast_pointer.next.next:
            #   slow pointer += 1
            slow_pointer = slow_pointer.next
            #   fast pointer += 2
            fast_pointer = fast_pointer.next.next
            #   if slow pointer == fast pointer then a loop is found, return True
            if slow_pointer == fast_pointer:
                return True
        # if loop ends, return False
        return False


