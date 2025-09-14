class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq=Counter(s)
        vowels="aeiou"
        v=0
        con=0
        for ch,c in freq.items():
            if ch in vowels:
                if c>v:
                    v=c
            else:
                if c>con:
                    con=c
        return v+con



        