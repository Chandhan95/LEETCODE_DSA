class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        def getmax_con():
            stack=[]
            res=0
            for i in range(n+1):
                while stack and (i==n or nums[stack[-1]]<=nums[i]):
                    mid=stack.pop()
                    if stack:
                        left=stack[-1]
                    else:
                        left=-1
                    right=i
                    res+=nums[mid]*(mid-left)*(right-mid)
                stack.append(i)
            return res
        def getmin_con():
            stack=[]
            res=0
            for i in range(n+1):
                while stack and (i==n or nums[stack[-1]]>=nums[i]):
                    mid=stack.pop()
                    if stack:
                        left=stack[-1]
                    else:
                        left=-1
                    right=i
                    res+=nums[mid]*(mid-left)*(right-mid)
                stack.append(i)
            return res
        return getmax_con()-getmin_con()