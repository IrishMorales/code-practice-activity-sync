class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(nlogn) solution with sort ---
        # keep largest_consecutive_count, current_consecutive_count
        # sort array, if nums[index] consecutive with nums[index-1], ++current_consecutive_count, update largest_consecutive_count if current is larger

        # set solution ---
        nums_set = set(nums)
        max_consecutive_found = 0

        # loop over nums, add nums[index] to a set
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num + 1
                while current_num in nums_set:
                    current_num += 1
                max_consecutive_found = max(current_num - num, max_consecutive_found)
        return max_consecutive_found
        # time complexity: O(n)
        # space complexity: O(n)
