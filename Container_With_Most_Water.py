class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        b=len(height)-1
        maxarea=0
        while(a<b):
            maxarea=max(min(height[a],height[b])*abs(a-b),maxarea)
            if(height[a]<height[b]):
                a=a+1
            else:
                b=b-1
        return(maxarea)
