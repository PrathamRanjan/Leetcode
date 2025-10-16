class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1
        
        top_k = sorted(frequency,key=frequency.get, reverse=True)[:k]
        return top_k
