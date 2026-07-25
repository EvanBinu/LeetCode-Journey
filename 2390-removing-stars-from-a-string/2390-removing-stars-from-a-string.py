class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        n = len(s)
        
        for i in range(n):
            if(s[i]=='*'):
                if(len(ans)!=0):
                    ans.pop()
            else:
                ans.append(s[i])    
        return "".join(ans)    