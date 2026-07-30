class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = {}
        left = 0
        ms = 0
        for right in range(len(fruits)):
            if fruits[right] in map:
                map[fruits[right]]+=1
            else:
                map[fruits[right]] = 1
            if len(map) > 2:
                if fruits[left] in map:
                    map[fruits[left]]-=1
                if map[fruits[left]] == 0:
                    del map[fruits[left]]
                left+=1
            ms = max(ms,right-left+1)
        return ms