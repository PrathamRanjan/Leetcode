class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def Success(k) -> bool:
            hours = 0
            for i in piles:
                hours = hours + (i + k -1)//k
            return hours <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right)//2
            if Success(mid):
                right = mid
            else:
                left = mid + 1
        return left
# still struggling to tell when to use binary search. 
    

