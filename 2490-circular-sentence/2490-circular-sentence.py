class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        last = 0
        for i in range(len(sentence)):
            if sentence[i]==' ':
                if sentence[i-1] != sentence[i+1]:
                    return False
        if sentence[-1] != sentence[0]:
            return False
        return True