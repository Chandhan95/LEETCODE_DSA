class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            alive=True
            while alive and a<0 and stack and stack[-1]>0:
                if stack[-1]<-a:
                    stack.pop()
                    continue
                elif stack[-1]==-a:
                    stack.pop()
                alive=False
            if alive:
                stack.append(a)
        return stack


