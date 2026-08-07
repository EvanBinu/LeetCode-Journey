class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = {}
        left = 0
        mlen = 0
        for right in range(len(fruits)):
            map[fruits[right]] = map.get(fruits[right],0)+1
            while len(map) > 2:
                map[fruits[left]]-=1
                if map[fruits[left]] <=0:
                    del map[fruits[left]]
                left+=1
            mlen = max(right-left+1,mlen)
        return mlen