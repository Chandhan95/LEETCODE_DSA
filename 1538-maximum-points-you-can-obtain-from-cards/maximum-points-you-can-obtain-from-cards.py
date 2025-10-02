class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total=sum(cardPoints)
        window_size=n-k
        curr_sum=sum(cardPoints[:window_size])
        min_sum=curr_sum
        for i in range(window_size,n):
            curr_sum+=cardPoints[i]-cardPoints[i-window_size]
            min_sum=min(min_sum,curr_sum)
        return total-min_sum