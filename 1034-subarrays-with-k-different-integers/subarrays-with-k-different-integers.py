class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(nums,k):
            count=defaultdict(int)
            n=len(nums)
            left=res=0
            for right in range(n):
                if count[nums[right]]==0:
                    k-=1
                count[nums[right]]+=1
                while k<0:
                    count[nums[left]]-=1
                    if count[nums[left]]==0:
                        k+=1
                    left+=1
                res+=right-left+1
            return res
        return atmost(nums,k)-atmost(nums,k-1)