class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area=0
        i=0
        j=len(heights)-1
        while i<j:
            current=min(heights[i],heights[j])*abs(i-j)
            max_area=max(max_area,current)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_area