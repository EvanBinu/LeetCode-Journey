class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a' : -1 ,'b' : -1, 'c': -1}
        cnt = 0
        n = len(s)
        for i in range(n):
            last_seen[s[i]] = i
            if last_seen['a']!= -1 and last_seen['b']!= -1 and last_seen['c']!= -1:
                cnt += min(last_seen['a'],last_seen['b'],last_seen['c']) + 1
        return cnt