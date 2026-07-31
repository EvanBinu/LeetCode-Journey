class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        map = {}
        maxfreq=maxlen=left= 0
        n = len(answerKey)
        for right in range(n):
            if answerKey[right] in map:
                map[answerKey[right]]+=1
            else:
                map[answerKey[right]]=1
            maxfreq = max(maxfreq,map[answerKey[right]])
            if (right-left+1) - maxfreq > k:
                map[answerKey[left]]-=1
                left+=1
            maxlen = max(maxlen,right-left+1)
        return maxlen