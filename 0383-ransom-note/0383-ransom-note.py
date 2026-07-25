class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapm = {}
        mapr = {}
        for c in magazine:
            if c in mapm:
                mapm[c]+=1
            else:
                mapm[c] = 1
        for c in ransomNote:
            if c in mapr:
                mapr[c]+=1
            else:
                mapr[c] = 1

        for c in ransomNote:
            if c in mapm:
                if mapm[c] < mapr[c]:
                    return False
            else:
                return False
        return True
