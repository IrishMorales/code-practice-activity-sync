class Solution:
    def romanToInt(self, s: str) -> int:
        # observation: when subtraction is used, only one of the smaller symbol is placed right before the larger one (ex. XXL not allowed)
        # observation: generally largest to smallest from left to right except when using subtraction

        symbol_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        # for each character check if it can be used to subtract from the next symbol, if it is parse the subtracted value and add to result
        for index in range(len(s)-1):
            current_value = symbol_values[s[index]]
            if current_value < symbol_values[s[index+1]]:
                result -= current_value
            else:
                result += current_value
        return result + symbol_values[s[-1]]
        # time complexity: O(n)
        # space complexity: O(1)
