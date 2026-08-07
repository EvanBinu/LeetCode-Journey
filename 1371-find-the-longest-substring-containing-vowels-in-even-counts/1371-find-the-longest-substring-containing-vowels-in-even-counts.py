class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        state = 0
        map = {"a" : 0, "e" : 1, "i" :2, "o" : 3, "u" : 4}
        frist = {0:-1}
        answer = 0
        for i in range(len(s)):
            if s[i] in map:
                state ^=(1<<map[s[i]])
            if state in frist:
                answer = max(answer,i - frist.get(state,0))
            if state not in frist:
                frist[state] = i
        return answer