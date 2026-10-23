class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1

        for i, num in enumerate(nums):
            if num != i:
                ans &= num
                ans &= i

        return 0 if ans == -1 else ans