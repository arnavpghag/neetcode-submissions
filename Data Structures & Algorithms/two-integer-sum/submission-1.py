class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, i in enumerate(nums):
            no2 = target - i
            if no2 in seen:
                return [seen[no2], idx]
            seen[i] = idx
        return [0]