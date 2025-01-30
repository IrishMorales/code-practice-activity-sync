class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        # naive solution ---
        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # answers[0] = [x for x in nums1_set if x not in nums2_set]
        # answers[1] = [x for x in nums2_set if x not in nums1_set]
        # return answers

        # time complexity: O(m + n + m^2 + n^2) where m, n is len(shorter nums), len(longer nums) -> reduces to O(n^2)
        # space complexity: O(2n) where n is len(longer nums) -> reduces to O(n)

        # optimal solution ---
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return [list(nums1_set.difference(nums2_set)), list(nums2_set.difference(nums1_set))]
