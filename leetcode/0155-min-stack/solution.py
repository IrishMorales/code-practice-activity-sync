class MinStack:
    def __init__(self):
        # initialize a linked list where head = top of stack
        self.head = self.Node()

    # each insert into the linked list will have the value itself and the minimum recorded so far
    def push(self, val):
        # if the value itself is lower than the minimum, minimum for that node = value
        min_val = min(val, self.head.min_val) if self.head.min_val is not None else val
        new_head = self.Node(val, self.head, min_val)
        self.head = new_head

    # pop = remove node at top of stack, set new head to head.next
    def pop(self):
        self.head = self.head.next

    # top = return head.val
    def top(self) -> int:
        return self.head.val

    # min = return head.min
    def getMin(self) -> int:
        return self.head.min_val

    class Node:
        def __init__(self, val=None, next=None, min_val=None):
            self.val = val
            self.next = next
            self.min_val = min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
