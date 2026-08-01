class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        s = numbers[r] + numbers[l]
        while l < r:
            if s > target:
                s-=numbers[r]
                r-=1
                s+=numbers[r]
            elif s < target:
                s-=numbers[l]
                l+=1
                s+=numbers[l]
            else:
                return [l+1,r+1]