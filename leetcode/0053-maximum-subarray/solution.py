class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            # either add the current num to the existim subarray sum or start a new subarray at current num
            current_sum = max(current_sum + num, num)
            # if max_sum > current_sum, update max_sum
            max_sum = max(current_sum, max_sum)
        return max_sum
        # time complexity: O(n)
        # space complexity: O(1)

