class Solution:
    def trimMean(self, arr: List[int]) -> float:
        s = 0
        n = len(arr)
        
        for i in range(int(n * 0.05)):
            arr.remove(min(arr))
            arr.remove(max(arr))
            
        
        for i in arr:
            s += i
            
        return s/len(arr)
            
    
            