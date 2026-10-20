class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for s in nums:
            if s-1 not in nums:
                j=0
                count=0
                while s+j in nums:
                    count+=1
                    if count>longest:
                        longest=count
                    j+=1
        return longest
