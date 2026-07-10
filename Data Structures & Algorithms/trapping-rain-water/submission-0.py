class Solution:
    def trap(self, height: List[int]) -> int:
        total =0
        l,r =0,len(height)-1
        lmax= height[0]
        rmax = height[len(height)-1]
        while l<r:
            if height[l] < height[r]:
                l+=1
                lmax = max(lmax,height[l])
                total += (lmax-height[l])
            else:
                r-=1
                rmax = max(rmax,height[r])
                total += (rmax-height[r])
        return total