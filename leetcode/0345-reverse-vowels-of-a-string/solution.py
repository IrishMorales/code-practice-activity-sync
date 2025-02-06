class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        # initial solution:
        # loop over s from end to start, store vowels found in an array
        # loop over s from start to end, for each vowel found replace with front of vowels array and remove from array
        # time complexity: O(2n)
        # space complexity: O(n)

        # optimal solution:
        # keep 2 pointers, 1 goes start -> end, other goes end -> start
        # start moves forward until it finds a vowel, end goes backward until it finds a vowel
        # when both have found a vowel, swap chars at start and end
        # stop and return string when start == end
        leftPointer = 0
        rightPointer = len(s)-1
        s = list(s)
        while leftPointer < rightPointer:
            if s[leftPointer] in vowels and s[rightPointer] in vowels:
                s[leftPointer], s[rightPointer] = s[rightPointer], s[leftPointer]
                leftPointer += 1
                rightPointer -= 1
            elif s[leftPointer] not in vowels:
                leftPointer += 1
            elif s[rightPointer] not in vowels:
                rightPointer -= 1
        return ''.join(s)
        # time complexity: O(2n)
        # space complexity: O(n)

