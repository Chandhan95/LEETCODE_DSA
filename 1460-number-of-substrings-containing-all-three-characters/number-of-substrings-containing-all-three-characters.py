class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans=0
        count={'a':0,'b':0,'c':0}
        left=0
        for right in range(len(s)):
            count[s[right]]+=1
            while count['a']>0 and count['b']>0 and count['c']>0:
                ans+=len(s)-right
                count[s[left]]-=1
                left+=1
        return ans