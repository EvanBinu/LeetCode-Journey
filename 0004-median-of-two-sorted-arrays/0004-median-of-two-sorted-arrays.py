class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1>n2:
            A,B = nums2,nums1
        else:
            A,B = nums1,nums2
        n1,n2 = len(A),len(B)
        l = 0
        r = n1 - 1
        total = n1+n2
        half = total//2
        while True:
            m1 = (l+r)//2
            m2 = half - m1 -2
            Aleft = A[m1] if m1>=0 else float("-inf")
            Bleft = B[m2] if m2 >= 0 else float("-inf")
            Aright = A[m1+1] if (m1+1) < n1 else float("inf")
            Bright = B[m2+1] if (m2+1) < n2 else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft > Bright:
                r = m1 - 1
            else:
                l = m1 + 1
                