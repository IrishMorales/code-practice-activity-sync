class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # initial solution --
        # loop over array, count number of positions where possible to insert flowerbed wo breaking the rule, compare to n
        # optimization 1: stop the loop upon reaching n positions
        # optimization 2: increment by 2 whenever setting a position to 1 because the next position cannot be planted in
        # time complexity: O(n)
        # space complexity: O(1)

        if n == 0:
            return True
            
        validSlots = 0
        for index in range(len(flowerbed)):
            if (flowerbed[index] == 0) and (index == 0 or flowerbed[index-1] == 0) and (index == len(flowerbed)-1 or flowerbed[index+1] == 0):
                validSlots += 1
                flowerbed[index] = 1
            if validSlots == n:
                return True
        return False

