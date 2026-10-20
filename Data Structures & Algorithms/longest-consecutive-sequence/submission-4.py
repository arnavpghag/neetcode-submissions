class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for i in nums:
            current=0
            if i-1 not in nums:
                currentnum=i
                current=1
                while currentnum+1 in nums :
                    current+=1
                    currentnum+=1
                if longest<current:
                    longest=current
        return longest    