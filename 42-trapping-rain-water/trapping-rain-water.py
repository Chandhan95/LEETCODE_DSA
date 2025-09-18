class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        leftmax=0
        rightmax=0
        water=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    water+=leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    water+=rightmax-height[right]
                right-=1
        return water
