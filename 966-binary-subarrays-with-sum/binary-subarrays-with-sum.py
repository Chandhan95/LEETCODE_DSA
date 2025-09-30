class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(goal):
            left=0
            ans=0
            for right in range(len(nums)):
                goal-=nums[right]
                while goal<0 and left<=right:
                    goal+=nums[left]
                    left+=1
                ans+=right-left+1
            return ans
        return atmost(goal)-atmost(goal-1)
