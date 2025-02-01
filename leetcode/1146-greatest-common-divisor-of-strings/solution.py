class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # look for largest subsequence in two sequences

        # unoptimized solution ---
        # longer_str = str1 if len(str1) > len(str2) else str2
        # longer_str_len = len(longer_str)
        # shorter_str = str1 if len(str1) <= len(str2) else str2
        # largest_substr = "" 
        # curr_substr = ""
        # shorter_str_index = 0
        # loop over longer_str {
        #     if (len(largest_substr) == longer_str_len) break
        #     if (shorter_str_index < len(shorter_str and longer_str[index] == shorter_str[shorter_str_index]) {
        #         curr_substr += longer_str[index]
        #         ++shorter_str_index
        #         if (len(curr_substr) > len(largest_substr)) {
        #             largest_substr = curr_substr
        #         }
        #     } else {
        #         curr_substr = ""
        #         shorter_str_index = 0
        #     }
        # }
        # return largest_substr

        # optimized solution ---
        # observation: gcd only exists if str1 + str2 == str2 + str1
        # observation: len(largest_substr) == gcd(len(str1), len(str2))
        return "" if (str1 + str2 != str2 + str1) else str1[:gcd(len(str1), len(str2))]
        # time complexity: O(N + M + logN) -> reduces to O(N)
        # space complexity: O(2N + 2M + gcd(N, M)) -> reduces to O(N)
