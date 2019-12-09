class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1 = len(word1)
        len_2 = len(word2)
        dp = [[-1] * (len_1 + 1) for x in range(len_2 + 1)]

        dp[0][0] = 0
        for i in range(1, len_1 + 1):
            dp[0][i] = i
        for j in range(1, len_2 + 1):
            dp[j][0] = j

        for i in range(1, len_2 + 1):
            for j in range(1, len_1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete = dp[i - 1][j] + 1
                    insert = dp[i][j - 1] + 1
                    replace = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(delete, insert, replace)

        for i in range(len_2 + 1):
            for j in range(len_1 + 1):
                print(dp[i][j], end='\t')
                if j == len_1:
                    print()

        return dp[len_2][len_1]

if __name__ == '__main__':
    sln = Solution()

    w1 = 'horse'
    w2 = 'ros'

    dis = sln.minDistance(w1, w2)
    print(dis)
