class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        map = {}
        maxfreq=maxlen=left= 0
        n = len(answerKey)
        for right in range(n):
            map[answerKey[right]] = map.get(answerKey[right],0)+1
            maxfreq = max(maxfreq,map[answerKey[right]])
            while (right-left+1) - maxfreq > k:
                map[answerKey[left]]-=1
                left+=1
            maxlen = max(maxlen,right-left+1)
        return maxlen