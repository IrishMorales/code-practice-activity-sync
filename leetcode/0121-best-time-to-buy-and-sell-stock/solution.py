class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # observation - ex. 2 input is a descending list, output is 0
        # observation - only need to return max profit, not indices
        # edge case: if prices has only one day, output is 0

        # general strategy ---
        # find the lowest price - buy
        # find the highest price after index of lowest price - sell

        # initial solution ---
        # do one pass over prices to keep track of the lowest price and its index
        # do one pass over prices subarray from lowest price to end of prices to keep track of highest price
        # return highest price after lowest price - lowest price
        # time complexity: O(2n) -> O(n)
        # space complexity: O(1)

        # optimal solution ---
        # buy = prices[0]
        # profit = 0
        # loop over prices[1:], if prices[index] < buy, buy = prices[index]; else if prices[index] - buy > profit, profit = prices[index] - buy
        # time complexity: O(n)
        # space complexity: O(1)
        
        buy = prices[0]
        profit = 0

        for index in range(1, len(prices)):
            if prices[index] < buy:
                buy = prices[index]
            elif (prices[index] - buy) > profit:
                profit = prices[index] - buy
        
        return profit

