class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # Optimization: If the smallest number is greater than 0,
            # three positive numbers can never sum to 0.
            if a > 0:
                break

            # Skip duplicate values for the first element
            if i > 0 and a == nums[i - 1]:
                continue

            # Two-pointer approach for the remaining two elements
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the second element
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res