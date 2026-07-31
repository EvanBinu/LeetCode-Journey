class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        k = len(t)
        n = len(s)
        for i in range(k):
            need[t[i]] = need.get(t[i],0)+1
        window={}
        formed =0
        required = len(need)
        left = 0
        minstring=""
        minlen = float("inf")
        start = 0   
        for right in range(n):
            ch = s[right]
            window[ch] = window.get(ch,0)+1
            if ch in need and window[ch] == need[ch]:
                formed+=1
            while formed == required:
                if right - left +1 < minlen:
                    minlen = right - left + 1
                    start = left
                lch = s[left]
                window[lch]-=1
                if lch in need and window[lch] < need[lch]:
                    formed-=1
                left+=1
        return "" if minlen == float(inf) else s[start:start+minlen]