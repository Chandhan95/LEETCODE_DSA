class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        left=0
        ans=0
        max_count=0
        count={}
        for right in range(n):
            count[s[right]]=count.get(s[right],0)+1
            max_count=max(max_count,count[s[right]])
            while (right-left+1)-max_count>k:
                count[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
