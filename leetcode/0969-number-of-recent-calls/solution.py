from collections import deque

# brute force solution ---
# requests = []
# requests.append(t)
# counter = 0
# loop over requests, if requests is in range [t - 3000, t], ++counter
# return counter
# time complexity: O(n^2) -> n is the number of pings
# space complexity: O(n)

# improved non-optimal solution ---
# requests = []
# requests.append(t)
# counter = 0
# loop over requests from end to start, if requests is in range [t - 3000, t], ++counter, if not break loop
# return counter
# time complexity: O(n^2) -> n is the number of pings
# space complexity: O(n)

# solution using queue ---
# only need to check 1st element
# requests = Queue()
# requests.queue(t)
# while requests[0] < t-3000, pop requests[0]
# return len(requests)
# time complexity: O(n) -> n is the number of pings
# space complexity: O(n)

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while (self.requests[0] < t-3000):
            self.requests.popleft() 
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
