class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0)+1
        arr = []
        for key,value in freq.items():
            arr.append([key,value])
        arr.sort(key = lambda x:x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(arr[i][0])
        print(arr)
        return result