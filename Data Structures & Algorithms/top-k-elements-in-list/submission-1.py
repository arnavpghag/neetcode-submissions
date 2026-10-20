class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers=Counter(nums)
        
        return heapq.nlargest(k, numbers, key=numbers.get)