class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # brute force solution ---
        # create a new array with the unique integers
        # loop over nums check if each num is seen before (i.e. in new array), if not append to array
        # time complexity: O(n^2) since outer loop is O(n), checking if num exists in new array is also O(n)

        # two pointer solution ---
        # loop over nums and keep a slow pointer and fast pointer
        # if fast pointer sees a number that isn't nums[slow_pointer], put it where slow pointer is
        slow_pointer = 0
        for num in nums[1:]:
            if num != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = num
        return slow_pointer + 1
