class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # initial solution ---
        # loop over nums, at each index compare sum of nums at left to sum of nums at right, upon reaching pivot index return index
        # if none after loop, return -1
        # time complexity: O(n^2)
        # space complexity: O(1)

        # optimal solution ---
        leftSum = 0
        rightSum = sum(nums)

        for index in range(len(nums)):
            if leftSum == (rightSum - nums[index]):
                return index
            else:
                leftSum += nums[index]
                rightSum -= nums[index]
        return -1
        # time complexity: O(n)
        # space complexity: O(1)
