class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        result = []
        right= 0
        left= 0
        for i in range(len(s)):
            last[s[i]] = i
        for i in range(len(s)):
            right = max(right,last[s[i]])
            if i == right:
                result.append(i-left+1)
                left = right+1
        return result
        

