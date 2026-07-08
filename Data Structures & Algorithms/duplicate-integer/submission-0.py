class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        bo = False
        for i,num in enumerate(nums):
            if num in seen:
                bo = True
                seen[num]+=1
            seen[num] =1
        return bo