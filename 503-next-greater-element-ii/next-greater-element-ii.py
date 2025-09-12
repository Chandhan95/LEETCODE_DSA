class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        n=len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[(i+j)%n]>nums[i]:
                    res[i]=nums[(i+j)%n]
                    break
        return res
        