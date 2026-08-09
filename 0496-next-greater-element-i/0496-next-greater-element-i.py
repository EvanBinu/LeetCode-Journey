class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        map ={}
        for i in range(n - 1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                map[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        result = []
        for x in nums1:
            result.append(map.get(x, -1))
        return result