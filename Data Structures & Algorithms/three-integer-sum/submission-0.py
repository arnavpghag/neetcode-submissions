class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target=0
        ans=set()
        nums.sort()
        for num in range(len(nums)):
            current=nums[num]
            i=num+1
            j=len(nums)-1
            while i<j:
                if target==nums[i]+nums[j]+current:
                    ans.add((current,nums[i],nums[j]))
                    i+=1
                    j-=1
                elif target<nums[i]+nums[j]+current:
                    j-=1
                else:
                    i+=1
        return [i for i in ans]