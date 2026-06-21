class Solution:
    def maxArea(self, height: List[int]) -> int:

        l=0
        r=len(height)-1
        maxx=0
        while l<r:
            w=r-l
            h=min(height[l],height[r])

            a=w*h
            maxx=max(a,maxx)

            if l<r:
                l+=1
            else:
                r-=1
        return maxx