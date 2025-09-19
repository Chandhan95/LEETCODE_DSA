class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        ple=[-1]*n
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                ple[i]=stack[-1]
            stack.append(i)
        nle=[n]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                nle[i]=stack[-1]
            stack.append(i)
        max_area=0
        for i in range(len(heights)):
            width=nle[i]-ple[i]-1
            area=heights[i]*width
            max_area=max(area,max_area)
        return max_area
        