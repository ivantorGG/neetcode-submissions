class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                best = max(curr, best)
                curr = 0

        return max(curr, best)
