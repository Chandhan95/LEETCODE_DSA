class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        if not s:
            return 0
        for i in range(0,len(s)):
            seen=set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len=max(max_len,j-i+1)
        return max_len