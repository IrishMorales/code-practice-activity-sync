class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force solution ---
        # loop looking at each word, loop over strs and check if each str is an anagram of that word
        # time complexity: O(n * n * isAnagramComplexity)
        # space complexity: O(n + isAnagramComplexity)

        # improved solution ---
        # for each word, sort the string and add it to a map if it isn't already existing in the map
        # key - sorted string; values - strings that match (anagrams) of that entry
        anagrams = {}
        for str_elem in strs:
            sorted_str = ''.join(sorted(str_elem))
            if sorted_str in anagrams.keys():
                anagrams[sorted_str].append(str_elem)
            else:
                anagrams[sorted_str] = [str_elem]
        return list(anagrams.values())
        # time complexity: O(n*mlogm) -> n is # of elements, m is length of longest str element
        # space complexity: O(n)
