class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        occ=float('-inf')
        count=0
        for x in nums:
            if occ <x+k:
                occ=max(occ+1,x-k)
                count+=1
        return count
