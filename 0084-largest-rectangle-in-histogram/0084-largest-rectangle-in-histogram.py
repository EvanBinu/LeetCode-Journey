class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        marea = 0
        n = len(heights)
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                j,h = stack.pop()
                marea = max(marea,h*(i-j))
                index = j
            stack.append((index,heights[i]))
        while stack:
            i,h = stack.pop()
            marea = max(marea,h*(n-i))
        return marea