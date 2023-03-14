class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

       
        lst = []
        
        for j in str(x):
            if j.isdigit() == False:
                 return False
            lst.append(int(j))
            
        
        for i in range(len(lst)):
            if lst[i] != lst[len(lst) - 1 -i]:
                return False


        return True