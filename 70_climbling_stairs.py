class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        L = [0] * 3
        L[0] = 1
        L[1] = 2
        for i in range(3, n+1):
            L[2] = L[0] + L[1]
            L[0] = L[1]
            L[1] = L[2]

        return L[2]

if __name__ == '__main__':
    sln = Solution()

    steps = sln.climbStairs(10)
    print(steps)
