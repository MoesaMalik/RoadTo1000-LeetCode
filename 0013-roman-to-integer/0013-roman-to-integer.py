class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {'I':1, 'V':5, 'X':10,'L':50,'C':100, 'D':500, 'M':1000}

        count = 0
        prev_value = 0

        for char in s:
            current_value = roman.get(char)
            if current_value > prev_value:
                count += current_value - 2 * prev_value
            else:
                count += current_value
            prev_value = current_value

        return count