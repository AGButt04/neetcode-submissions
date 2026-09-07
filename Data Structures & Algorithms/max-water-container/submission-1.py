class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        maxA = 0
        left = 0
        right = length - 1

        while left < right:
            width = right - left
            length = min(heights[left], heights[right])
            currA = width * length
            maxA = max(maxA, currA)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return maxA