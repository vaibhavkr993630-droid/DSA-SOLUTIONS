class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for num in arr1:
            if all(abs(num - x) > d for x in arr2):
                count += 1

        return count