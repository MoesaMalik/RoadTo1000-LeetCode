class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        hm = {}
        
        
        for i in arr:
            
            if i not in hm.keys():
                hm[i] = 1
            
            else:
                hm[i] += 1   
            
            
            
        return len(hm.values()) == len(set(hm.values()))            
            
                