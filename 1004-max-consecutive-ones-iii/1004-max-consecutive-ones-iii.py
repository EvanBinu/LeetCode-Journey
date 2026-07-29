class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mlen,zeros,left = 0,0,0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros+=1
            if zeros > k:
                if nums[left] == 0:
                    zeros-=1
                left+=1
            if zeros <=k:
                mlen = max(mlen,right-left+1)
        return mlen