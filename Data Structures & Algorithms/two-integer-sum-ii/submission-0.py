class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum == target:
                # 1-indexed, so add 1 to both indices
                return [l + 1, r + 1]
            elif cur_sum < target:
                l += 1
            else:
                r -= 1