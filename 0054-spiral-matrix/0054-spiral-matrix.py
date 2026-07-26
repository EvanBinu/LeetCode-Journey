class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rf,cf = 0,0
        rl = len(matrix)-1
        cl = len(matrix[0])-1
        i,j=0,0
        ans = []
        while rf <= rl and cf <= cl:
            for i in range(cf,cl+1):
                ans.append(matrix[rf][i])
            rf+=1
            for j in range(rf,rl+1):
                ans.append(matrix[j][cl])
            cl-=1
            if rf <=rl:
                for i in range(cl,cf-1,-1):
                    ans.append(matrix[rl][i])
                rl-=1
            if cf <=cl:
                for j in range(rl,rf-1,-1):
                    ans.append(matrix[j][cf])
                cf+=1
        return ans
