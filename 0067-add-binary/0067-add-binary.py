class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        dec1 = 0
        dec2 = 0
        for i in range(len(a)):

            dec1 += int(a[i]) * pow(2,(len(a) - i -1))
        
        for j in range(len(b)):

            dec2 += int(b[j]) * pow(2,(len(b) - j -1))

        res = dec1 + dec2

        return bin(res)[2:]
