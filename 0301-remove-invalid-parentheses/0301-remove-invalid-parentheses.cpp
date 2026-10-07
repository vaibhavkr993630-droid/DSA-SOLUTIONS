// class Solution {
// public:
//     vector<string> removeInvalidParentheses(string s) {
        
//     }
// };
class Solution {
public:
    unordered_set<string> ans;

    void solve(string &s, int idx, int leftRem, int rightRem,
               int balance, string curr) {

        if (idx == s.size()) {
            if (leftRem == 0 && rightRem == 0 && balance == 0) {
                ans.insert(curr);
            }
            return;
        }

        // Current character is '('
        if (s[idx] == '(') {

            // Option 1: remove it
            if (leftRem > 0) {
                solve(s, idx + 1, leftRem - 1, rightRem,
                      balance, curr);
            }

            // Option 2: keep it
            solve(s, idx + 1, leftRem, rightRem,
                  balance + 1, curr + '(');
        }

        // Current character is ')'
        else if (s[idx] == ')') {

            // Option 1: remove it
            if (rightRem > 0) {
                solve(s, idx + 1, leftRem, rightRem - 1,
                      balance, curr);
            }

            // Option 2: keep it only if it doesn't make
            // the balance negative
            if (balance > 0) {
                solve(s, idx + 1, leftRem, rightRem,
                      balance - 1, curr + ')');
            }
        }

        // Letter
        else {
            solve(s, idx + 1, leftRem, rightRem,
                  balance, curr + s[idx]);
        }
    }

    vector<string> removeInvalidParentheses(string s) {

        int leftRem = 0;
        int rightRem = 0;

        // Find minimum number of '(' and ')' to remove
        for (char c : s) {
            if (c == '(') {
                leftRem++;
            }
            else if (c == ')') {
                if (leftRem > 0) {
                    leftRem--;
                }
                else {
                    rightRem++;
                }
            }
        }

        string curr;
        solve(s, 0, leftRem, rightRem, 0, curr);

        return vector<string>(ans.begin(), ans.end());
    }
};