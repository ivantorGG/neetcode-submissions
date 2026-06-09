class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                best = max(best, right - left)
                left = right

                while left < len(nums) and nums[left] == 0:
                    left += 1

        best = max(best, right - left + 1)
        return best
