class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        heights.append(0)
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                h = heights[index]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                area = max(area,h*w)
            stack.append(i)

        return area