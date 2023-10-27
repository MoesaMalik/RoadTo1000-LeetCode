class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        maxCount = 0
        start = 0
        char_index = {}  # Dictionary to store the last seen index of each character
        
        for i in range(len(s)):
            if s[i] in char_index and char_index[s[i]] >= start:
                start = char_index[s[i]] + 1
            char_index[s[i]] = i
            maxCount = max(maxCount, i - start + 1)
        
        return maxCount