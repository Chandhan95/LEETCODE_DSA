class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nge=[-1]*len(nums2)
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                nge[i]=stack[-1]
            stack.append(nums2[i])
        res=[]
        for num in nums1:
            index=nums2.index(num)
            res.append(nge[index])
        return res
            

        