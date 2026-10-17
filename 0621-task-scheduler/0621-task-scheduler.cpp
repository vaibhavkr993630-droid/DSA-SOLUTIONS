
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26, 0);

        for (int i = 0; i < tasks.size(); i++) {
            freq[tasks[i] - 'A']++;
        }

        priority_queue<pair<int, char>> pq;

        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                pq.push({freq[i], char('A' + i)});
            }
        }

        queue<pair<int, char>> q;

        int remainingTasks = tasks.size();
        int ans = 0;

        while (remainingTasks > 0) {

            // n + 1 intervals have elapsed:
            // the oldest task can become available.
            if (q.size() == n + 1) {
                auto p = q.front();
                q.pop();

                if (p.first > 0) {
                    pq.push(p);
                }
            }

            if (!pq.empty()) {
                auto z = pq.top();
                pq.pop();

                z.first--;
                remainingTasks--;
                ans++;

                if (z.first > 0) {
                    q.push(z);
                } else {
                    q.push({-1, '#'}); // Dummy interval
                }
            }
            else {
                // CPU is idle, but time still passes.
                q.push({-1, '#'});
                ans++;
            }
        }

        return ans;
    }
};
