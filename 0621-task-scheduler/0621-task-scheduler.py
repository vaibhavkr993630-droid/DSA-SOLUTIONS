
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # Python heapq is a min heap, so use negative frequencies.
        pq = []

        for i in range(26):
            if freq[i] > 0:
                heapq.heappush(pq, (-freq[i], chr(ord('A') + i)))

        q = deque()
        remainingTasks = len(tasks)
        ans = 0

        while remainingTasks > 0:

            # Release the oldest cooldown entry after n + 1 intervals.
            if len(q) == n + 1:
                p = q.popleft()

                if p[0] < 0:  # Real task with remaining frequency
                    heapq.heappush(pq, p)

            if pq:
                z = heapq.heappop(pq)

                remaining_freq = -z[0] - 1
                remainingTasks -= 1
                ans += 1

                if remaining_freq > 0:
                    q.append((-remaining_freq, z[1]))
                else:
                    q.append((0, '#'))  # Dummy interval
            else:
                # No available task: CPU remains idle.
                q.append((0, '#'))
                ans += 1

        return ans

        