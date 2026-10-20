class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right=[]
        left=[]

        mul=1
        for i in range(len(nums)):
            right.append(mul)
            mul*=nums[i]
        
        mul2=1
        j=len(nums)-1
        while j>=0:
            left.append(mul2)
            mul2*=nums[j]
            
            j=j-1

        left=left[::-1]
        return [a*b for a,b in zip(right,left)]
