class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # dp[j] = length of longest valid subsequence ending at column j
        dp = [1] * m
        
        for j in range(m):
            for i in range(j):
                # Check if column i can come before column j
                # For all rows, strs[row][i] <= strs[row][j]
                valid = True
                for row in range(n):
                    if strs[row][i] > strs[row][j]:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # Answer is total columns minus longest valid subsequence
        return m - max(dp)