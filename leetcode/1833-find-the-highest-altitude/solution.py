class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        # initial and optimal solution ---
        # currentAlt = highestAlt = 0

        # loop over gain {
        #     currentAlt += gain[index]
        #     highestAlt = max(currentAlt, highestAlt)
        # }

        # return highestAlt

        # time complexity: O(n)
        # space complexity: O(1)

        currentAlt = highestAlt = 0

        for index in range(len(gain)):
            currentAlt += gain[index]
            highestAlt = max(currentAlt, highestAlt)

        return highestAlt

