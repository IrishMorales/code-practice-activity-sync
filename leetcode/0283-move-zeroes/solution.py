class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # naive solution ----
        # loop over arr {
        #     if (arr[index] == 0) zero_counter += 1, pop arr[index]
        # }
        # return arr + push 0s to end based on zero_counter

        # in real life development, I would write this as arr.countZeroes, arr.popZeros, arr.pushZeroes
        # for readability (KISS principle and readability > optimal/clever solutions that are less readable)

        # time complexity: O(n) -> n = length of array, however, dependent on complexity of array pop in language
        # space complexity: O(1) -> constant 


        # optimal solution ---
        # loop over arr {
        #     if (arr[index]) != 0, arr[lastNonzeroAt++] = arr[index]
        # }

        # loop over arr[lastNonzeroAt:end] {
        #     arr[index] = 0
        # }
        # time complexity: O(n) -> n = length of array
        # space complexity: O(1) -> constant 

        lastNonzeroAt = 0

        for index in range(len(nums)):
            if (nums[index] != 0):
                nums[lastNonzeroAt] = nums[index]
                lastNonzeroAt += 1
        
        for index in range(lastNonzeroAt, len(nums)):
            nums[index] = 0

