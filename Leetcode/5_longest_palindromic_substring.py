class Solution:
    # DP
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s == 1:
            return s

        dp = [[False for i in range(len_s)] for i in range(len_s)]
        max_len = 0
        substr = ''

        for right in range(len_s):
            for left in range(right + 1):
                if s[left] == s[right] and ( (right - left <= 2) or dp[left + 1][right - 1] ):
                    dp[left][right] = True
                    if right - left + 1 > max_len:
                        max_len = right - left + 1
                        substr = s[left:right + 1]

        for left in range(len_s):
            for right in range(len_s):
                print(dp[left][right], end='\t')
                if right == len_s - 1:
                    print()

        return substr

    # Manacher
    def manacher(self, s: str) -> str:
        s = '#' + '#'.join(s) + '#'

        RL = [0] * len(s)
        MaxRight = 0
        pos = 0

        for i in range(len(s)):
            if i < MaxRight:
                RL[i] = min(RL[pos-i + pos], MaxRight - i)
            else:
                RL[i] = 1

            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1

            if RL[i] > MaxRight:
                MaxRight = RL[i]
                pos = i

        substr = ''
        for x in s[pos - MaxRight + 1 : pos + MaxRight].split('#'):
            substr += x
        return substr

if __name__ == '__main__':
    sln = Solution()

    s1 = 'abcdccc'

    # string = sln.longestPalindrome(s1)
    string = sln.manacher(s1)
    print('s1 : ' + s1)
    print('substring : ' + string)
