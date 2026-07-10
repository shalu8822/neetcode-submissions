class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total =0
        l,r =0,len(heights)-1
        maxarea = 0
        currarea =0
        while(l<r):
            currarea = min(heights[l],heights[r]) * (r-l)
            maxarea = max(maxarea,currarea)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
        '''
        lmax= heights[0]
        rmax = heights[len(heights)-1]
        while l<r:
            if heights[l] < heights[r]:
                l+=1
                lmax = max(lmax,heights[l])
                total += (lmax-heights[l])
            else:
                r-=1
                rmax = max(rmax,heights[r])
                total += (rmax-heights[r])
        return total
        '''