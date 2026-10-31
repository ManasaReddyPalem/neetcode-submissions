class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        # freq_buckets[i] will store all numbers that appear exactly i times
        freq_buckets = [[] for _ in range(len(nums) + 1)]

        # Step 1: Count frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Group numbers by their frequency
        for n, c in count.items():
            freq_buckets[c].append(n)

        # Step 3: Gather the top k elements starting from the highest frequency
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res