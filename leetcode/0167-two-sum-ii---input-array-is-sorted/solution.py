class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initial solution ---
        # keep a slow_pointer and fast_pointer
        # loop slow_pointer over numbers
        #   loop fast_pointer over numbers until we find target - slow_pointer, return slow_pointer and fast_pointer
        # time complexity: O(n^2)
        # space complexity: O(1)

        # optimal solution ---
        # keep a pointer at start and pointer at end
        start = 0
        end = len(numbers)-1

        while True:
            current_sum = numbers[start] + numbers[end]
            if current_sum == target:
                return [start+1, end+1]
            elif current_sum < target:
                start += 1
            else:
                end -= 1

        # time complexity: O(n)
        # space complexity: O(1)

