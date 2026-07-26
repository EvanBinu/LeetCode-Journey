class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = []
        for i in range(1,n*n+1):
            arr.append(i)
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        i = 0
        matrix = [[0]*n for _ in range(n)]
        while top <= bottom and left <= right:
            for j in range(left,right+1):
                matrix[top][j] = arr[i]
                i+=1
            top+=1
            for j in range(top,bottom+1):
                matrix[j][right] = arr[i]
                i+=1
            right-=1
            if top <= bottom:
                for j in range(right,left-1,-1):
                    matrix[bottom][j] = arr[i]
                    i+=1
                bottom-=1
            if left <=right:
                for j in range(bottom,top-1,-1):
                    matrix[j][left] = arr[i]
                    i+=1
                left+=1
        return matrix