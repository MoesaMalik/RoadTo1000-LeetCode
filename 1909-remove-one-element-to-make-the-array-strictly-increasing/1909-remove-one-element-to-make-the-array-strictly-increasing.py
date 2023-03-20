class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        for i, val in enumerate(nums):
            new_nums = nums[:i] + nums[i + 1:]
            if new_nums == sorted(list(set(new_nums))):
                return True
        return False
        
        
        
        
        
    
            