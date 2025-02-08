class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initial solution (binary search -> O(logn)) ---
        # left = 0
        # right = len(nums)-1

        # while left <= right:
        #     # get the middle index of the array
        #     mid = (left + right) // 2

        #     # if target == nums[index], return index
        #     if target == nums[mid]:
        #         return mid
        #     # if target is higher than nums[index], repeat step above (continue to next loop iteration) with array of elements above index
        #     elif target > nums[mid]:
        #         left = mid + 1
        #     # if target is lower than nums[index], repeat step above (continue to next loop iteration) with array of elements below index
        #     else:
        #         right = mid - 1
        
        # return -1
        # time complexity: O(logn)
        # space complexity: O(1)

        # built-in solution ---
        # returns the first index to the right of the target (i.e. where the target can be inserted)
        index = bisect.bisect_right(nums, target)
        if index > 0 and nums[index - 1] == target:
            return index - 1
        else:
            return -1
        # time complexity: O(logn)
        # space complexity: O(1)
