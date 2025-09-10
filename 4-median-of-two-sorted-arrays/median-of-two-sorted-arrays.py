class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if len(nums1)%2==0:
            x=nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1]
            return x/2
        else:
            x=nums1[len(nums1)//2]
            return x