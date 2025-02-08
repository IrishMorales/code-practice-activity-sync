class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initial solution ---
        # keep two pointers, one is a slow pointer, one is a fast pointer
        # loop slowPointer over nums {
        #   loop fastPointer over nums {
        #       if slowPointer == fastPointer, continue to next iteration of fastPointer loop
        #       if nums[slowPointer] + nums[fastPointer] == target, return [slowPointer, fastPointer]
        #   }
        # }
        # time complexity: O(n^2)
        # space complexity: O(1)

        # optimal solution in terms of speed (using hash table) ---
        hashmap = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in hashmap:
                return [index, hashmap[complement]]
            hashmap[nums[index]] = index
        # time complexity: O(n)
        # space complexity: O(n)

