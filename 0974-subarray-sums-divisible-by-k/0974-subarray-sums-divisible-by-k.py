class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        prefix = 0
        answer = 0
        for i in range(len(nums)):
            prefix +=nums[i]
            rem = prefix%k
            if rem < 0:
                rem = (rem%k+k)%k
            if rem in freq:
                answer+=freq[rem]
                freq[rem]+=1
            else:
                freq[rem] =1
        return answer