class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        changed=True
        while changed:
            changed=False
            i=0
            while i<len(asteroids)-1:
                if asteroids[i]>0 and asteroids[i+1]<0:
                    if abs(asteroids[i])>abs(asteroids[i+1]):
                        asteroids.pop(i+1)
                    elif abs(asteroids[i])<abs(asteroids[i+1]):
                        asteroids.pop(i)
                    else:
                        asteroids.pop(i)
                        asteroids.pop(i)
                    changed=True
                    break
                i+=1
        return asteroids