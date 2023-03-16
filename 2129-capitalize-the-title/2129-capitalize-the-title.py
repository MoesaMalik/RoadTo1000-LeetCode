class Solution:
    def capitalizeTitle(self, title: str) -> str:
        strlst = title.split()
    
        for i, c in enumerate(strlst):
            if len(c) > 2:
                strlst[i] = c.capitalize()
            else:
                strlst[i] = c.lower()
            
        return ' '.join(strlst)
            
                
                