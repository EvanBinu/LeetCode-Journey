class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map = {}
        for x in arr:
            if x in map:
                map[x]+=1
            else:
                map[x] = 1
        ans = []
        for x in arr:
            if x == map[x]:
                ans.append(x)
        if(len(ans) > 0):
            return max(ans)
        else:
            return -1