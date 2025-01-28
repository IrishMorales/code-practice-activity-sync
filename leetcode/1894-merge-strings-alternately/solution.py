class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # loop {
        #     if (word1) append to final_word
        #     if (word2) append to final_word
        # }
        # time complexity: O(m + n) -> m is the length of the shorter word, n is the length of the longer word
        # space complexity: O(m + n) -> if considering space during processing
        # space complexity: O(1) -> if only considering space of output

        word1_len = len(word1)
        word2_len = len(word2)
        longer_word_len = max(word1_len, word2_len)
        new_word = ""

        for index in range(0, longer_word_len):
            if (index < word1_len):
                new_word += word1[index]
            if (index < word2_len):
                new_word += word2[index]
        
        return new_word
