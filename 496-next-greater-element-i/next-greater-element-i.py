class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for num in nums1:
            index=nums2.index(num)
            ans=-1
            for i in range(index+1,len(nums2)):
                if nums2[i]>num:
                    ans=nums2[i]
                    break
            res.append(ans)
        return res

        