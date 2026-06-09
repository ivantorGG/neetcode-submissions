class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = right = 0

        while left < len(nums) and right < len(nums):
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1

            elif nums[left] != val:
                left += 1
                right = left + 1
            else:
                right = left + 1
                while right < len(nums) and nums[right] == val:
                    right += 1

        while left < len(nums) and nums[left] != val:
            left += 1

        return left
