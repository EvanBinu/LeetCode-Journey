class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        i,j=0,0
        n = len(fruits)
        count = 0

        while i < n:
            if fruits[i] <= baskets[j]:
                count+=1
                i+=1
                baskets.pop(j)
                j=0
            else:
                if j == len(baskets) - 1:
                    j = 0
                    i +=1
                else:
                    j+=1

        return n-count