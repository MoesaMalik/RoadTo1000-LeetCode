class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}
        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        for j in hm.keys():
            if hm.get(j) > (len(nums)//2):
                return j
        return -1
            
