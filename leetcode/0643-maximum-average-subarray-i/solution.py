class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # initial solution ---

        # maxAverage = -infinity
        # loop over arr {
        #     currentAverage = average(arr[index:index+k])
        #     if (currentAverage > maxAverage) maxAverage = currentAverage
        # }
        # return maxAverage

        # time complexity: O(n * time complexity of average() implementation) -> reduces to O(n)
        # space complexity: O(1)

        # optimal solution ---

        # currSum = maxSum = sum(arr[0:k])
        # loop over arr[1:len(arr)-k] {
        #     currSum -= element to left of array (arr[index-1])
        #     currSum += element at end of array (arr[index+k-1])
        #     if (currSum > maxSum) maxSum = currSum
        # }
        # return currSum/k

        # time complexity: O(n)
        # space complexity: O(1)

        currSum = maxSum = sum(nums[:k])

        for index in range(1, len(nums)-k+1):
            currSum -= nums[index-1]
            currSum += nums[index+k-1]
            if (currSum > maxSum):
                maxSum = currSum
            print(index)

        return float(maxSum)/k
