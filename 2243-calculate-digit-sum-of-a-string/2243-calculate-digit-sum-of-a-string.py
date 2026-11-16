
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]
                digit_sum = sum(int(ch) for ch in group)
                res += str(digit_sum)

            s = res

        return s
