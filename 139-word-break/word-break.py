class Solution(object):
    def wordBreak(self, s, wordDict):
        maxlen = max(len(word) for word in wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(max(0, i - maxlen), i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]