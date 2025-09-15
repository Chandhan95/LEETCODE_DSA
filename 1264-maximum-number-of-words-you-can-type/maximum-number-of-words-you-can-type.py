class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken=set(brokenLetters)
        words=text.split()
        count=0
        for word in words:
            if all(ch not in broken for ch in word):
                count+=1
        return count