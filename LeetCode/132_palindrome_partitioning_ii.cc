/*
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut. 
*/

// Dynamic programming. Store 1-d array indicating the min-cut for s[0, i) prefix. 
// Update the minCuts for substrings as we check the strings.
// j = 0 is needed in this case.

class Solution {
    public:
        int minCut(string s) {
            if (s.empty()) return 0;
    
            int n = s.size();
    
            // minCuts[i] = minimum cuts needed for substring s[0:i)
            // (i.e., the prefix of length i)
            vector<int> minCuts(n + 1, INT_MAX);
    
            // Define empty prefix cut count as -1 so that when a whole prefix
            // is a palindrome we get: minCuts[r+1] = minCuts[0] + 1 = 0
            minCuts[0] = -1;
    
            // Treat each position i as the center of a palindrome
            for (int i = 0; i < n; ++i) {
    
                // Expand around center i for odd-length palindromes
                // palindrome range becomes [i-j, i+j]
                for (int j = 0; i - j >= 0 && i + j < n && s[i-j] == s[i+j]; ++j) {
    
                    int left = i - j;
                    int right = i + j;
    
                    // If s[left:right] is palindrome, update minimum cuts
                    // for prefix ending at right
                    minCuts[right + 1] = min(minCuts[right + 1],
                                             minCuts[left] + 1);
                }
    
                // Expand around center between i and i+1 for even palindromes
                // palindrome range becomes [i-j, i+j+1]
                for (int j = 0; i - j >= 0 && i + j + 1 < n && s[i-j] == s[i+j+1]; ++j) {
    
                    int left = i - j;
                    int right = i + j + 1;
    
                    minCuts[right + 1] = min(minCuts[right + 1],
                                             minCuts[left] + 1);
                }
            }
    
            // minCuts[n] stores the minimum cuts for the whole string
            return minCuts[n];
        }
    };

