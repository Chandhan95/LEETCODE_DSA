class Solution:
    def triangleType(self, nums: List[int]) -> str:
        count=1
        nums.sort()
        if nums[0]+nums[1]<=nums[2]:
            return "none"
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
        if count==3:
            return "equilateral"
        elif count==2:
            return "isosceles"
        else :
            return "scalene"
       