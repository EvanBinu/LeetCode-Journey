class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        elif k > 0:
            ans = [0]*len(code)
            for i in range(len(code)):
                val = 0
                for j in range(1,k+1):
                    val+=code[(i+j)%len(code)]
                ans[i] = val
            return ans
        else:
            ans = [0]*len(code)
            for i in range(len(code)):
                val = 0
                for j in range(1,-k+1):
                    val+=code[(i-j)%len(code)]
                ans[i] = val
            return ans