class Solution:
        
    def search(self, nums: List[int], target: int) -> int:
        '''if target in nums:
            return nums.index(target)
        else:
            return -1'''
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = l+(h-l)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                h = mid-1
            else:
                l = mid+1
        return -1

        