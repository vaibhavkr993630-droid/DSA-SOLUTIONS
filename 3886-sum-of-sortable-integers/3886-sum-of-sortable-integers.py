class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            prev_max = float('-inf')
            sortable = True

            for i in range(0, n, k):
                arr = nums[i:i + k]
                m = len(arr)

                # Find whether this block can be rotated
                # into non-decreasing order.
                drops = 0
                for j in range(m):
                    if arr[j] > arr[(j + 1) % m]:
                        drops += 1

                if drops > 1:
                    sortable = False
                    break

                # Minimum and maximum values of this block
                # remain unchanged under rotation.
                if min(arr) < prev_max:
                    sortable = False
                    break

                prev_max = max(arr)

            if sortable:
                ans += k

        return ans