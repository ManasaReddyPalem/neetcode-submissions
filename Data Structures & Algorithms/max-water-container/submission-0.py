class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            # Area = width * min(height at l, height at r)
            width = r - l
            h = min(heights[l], heights[r])
            current_water = width * h
            
            max_water = max(max_water, current_water)

            # Move the pointer pointing to the shorter bar
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water
