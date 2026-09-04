class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        length = len(nums)
        nums.sort()

        for i in range(length):
            curr = nums[i]
            if i > 0 and nums[i - 1] == curr:
                continue
            left = i + 1
            right = length - 1

            while left < length and left < right:
                summ = curr + nums[left] + nums[right]
                if summ == 0:
                    triplets.append([curr, nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                elif summ > 0:
                    right -= 1
                else: 
                    left += 1
        
        return triplets

