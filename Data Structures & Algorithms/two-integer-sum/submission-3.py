class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}

        for idx, n in enumerate(nums):
            if (target - n) in prev_nums:
                return [prev_nums[target - n], idx]
            
            prev_nums[n] = idx
        
        return []