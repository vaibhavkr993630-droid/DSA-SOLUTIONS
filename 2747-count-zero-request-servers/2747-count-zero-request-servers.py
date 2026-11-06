class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        q = sorted([(t, i) for i, t in enumerate(queries)])

        freq = {}
        left = right = 0
        ans = [0] * len(queries)
        active = 0

        for t, idx in q:
            while right < len(logs) and logs[right][1] <= t:
                server = logs[right][0]
                freq[server] = freq.get(server, 0) + 1
                if freq[server] == 1:
                    active += 1
                right += 1

            while left < right and logs[left][1] < t - x:
                server = logs[left][0]
                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans