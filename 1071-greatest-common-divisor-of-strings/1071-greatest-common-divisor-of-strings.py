class Solution:
    def helper(self,a,b):
        while b > 0:
            a,b = b,a%b
        return a
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        l = self.helper(len(str1),len(str2))
        return str1[:l]
        