class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        maps = {}
        mapt = {}
        for i in range(len(s)):
            if s[i] in maps:
                if maps[s[i]]!=t[i]:
                    return False
            else:
                maps[s[i]] = t[i]
            if t[i] in mapt:
                if mapt[t[i]] != s[i]:
                    return False
            else:
                mapt[t[i]] = s[i]
        return True   
        