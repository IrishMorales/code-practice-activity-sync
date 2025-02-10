class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force solution ---
        # keep a slow pointer (outer loop) and fast pointer (inner loop)
        # for each slow pointer value, go over nums with your fast pointer and multiply until you have the answer[i]
        # time complexity: O(n^2)
        # space complexity: O(1)

        # optimal solution ---
        # start with ans being an array with all 1s
        output = [1]*len(nums)

        # do two passes, one going forward and multiplying all numbers before ans[i] to ans[i] (keep the product in a variable)
        before_nums_product = 1
        for index in range(len(nums)):
            output[index] *= before_nums_product
            before_nums_product *= nums[index]
        
        # one pass going backward and multiplying all numbers after ans[i] to ans[i] (keep the product in a variable)
        after_nums_product = 1
        for index in range(len(nums)-1, -1, -1):
            output[index] *= after_nums_product
            after_nums_product *= nums[index]
        
        return output
        # time complexity: O(n)
        # space complexity: O(1)
