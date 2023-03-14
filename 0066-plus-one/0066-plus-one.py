class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                
                if i == 0:
                    digits [i] = 0
                    digits = [1] + digits
                    break
                

                    
                    break
                digits[i] = 0
        
        return digits
               