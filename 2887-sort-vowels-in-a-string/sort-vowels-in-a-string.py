class Solution:
    def sortVowels(self, s: str) -> str:
        store=[]
        ans=""
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                store.append(s[i])
        store.sort()
        j=0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                ans+=store[j]
                j+=1
            else:
                ans+=s[i]
        return ans
                
