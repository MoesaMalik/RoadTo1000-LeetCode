class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)> len(t):
            return False
        
        if len(s)==0:
            return True
        
        
        j = 0
        for i in range(len(t)):
            if j <= len(s)-1:
                if s[j] == t[i]:
                    j +=1
                
            
        return len(s) == j
