class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers={}
        for i in nums:
            if i in numbers:
                numbers[i]+=1
            else:
                numbers[i]=1
        
        return heapq.nlargest(k, numbers, key=numbers.get)