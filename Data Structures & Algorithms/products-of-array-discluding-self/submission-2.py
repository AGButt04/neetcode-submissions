class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        prefix = 1
        suffix = 1
        
        for num in nums:
            products.append(prefix)
            prefix *= num
        
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]

        return products