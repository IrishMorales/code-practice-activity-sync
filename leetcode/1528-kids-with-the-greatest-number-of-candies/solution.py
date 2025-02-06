class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # initial (optimal) solution ---
        # get greatest in initial array (O(n)), then loop over array and check if array[index] >= max (O(n))
        # time complexity: O(n)
        # space complexity: O(1)

        maxCandies = max(candies)
        result = []
        for candy in candies:
            result.append(True) if candy + extraCandies >= maxCandies else result.append(False)
        
        return result
                
