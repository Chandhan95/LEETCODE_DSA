class Solution:
    def largestrectanglearea(self,heights):
        n=len(heights)
        ple=[-1]*n
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                stack.pop()
            if stack:
                ple[i]=stack[-1]
            stack.append(i)
        nle=[n]*n
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                nle[i]=stack[-1]
            stack.append(i)
        max_area=0
        for i in range(n):
            width=nle[i]-ple[i]-1
            max_area=max(max_area,width*heights[i])
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n=len(matrix)
        m=len(matrix[0])
        heights=[0]*m
        max_area=0
        for row in matrix:
            for j in range(m):
                if row[j]=="1":
                    heights[j]+=1
                else:
                    heights[j]=0
            max_area=max(max_area,self.largestrectanglearea(heights))
        return max_area
        