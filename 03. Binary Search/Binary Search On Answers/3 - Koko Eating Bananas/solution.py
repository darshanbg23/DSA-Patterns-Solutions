class Solution:

    def totalHours(self, nums, hour):
        n = len(nums)
        total = 0

        for i in range(n):
            total += math.ceil(nums[i] / hour)

        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        maxi = max(piles)
        low, high = 1, maxi

        while low <= high:

            mid = (low + high) // 2

            res = self.totalHours(piles, mid)

            if res <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low