class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

       
        hm = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in hm:
                stack.append(c)
            elif not stack or hm[stack.pop()] != c:
                return False
        return not stack
           

