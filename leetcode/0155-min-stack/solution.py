class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head == None:
            self.head = self.Node(val, val, None)
        else:
            self.head = self.Node(val, min(val, self.head.min_val), self.head)

    def pop(self) -> None:
        self.head = self.head.next_node

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_val

    class Node:
        def __init__(self, val: int, min_val: int, next_node):
            self.val = val
            self.min_val = min_val
            self.next_node = next_node

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
