from typing import List

class Solution:

    # 我的解法，改了三四个版本，仍然是超时的，时间复杂度总是O(n^2)
    def my_countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) == 0:
            return 0

        dp = [nums[0]]
        num = 0
        if lower <= dp[0] <= upper:
                num += 1

        for i in range(1, len(nums)):
            dp.append(dp[i-1] + nums[i])
            if lower <= dp[i] <= upper:
                num += 1

        while len(dp) > 1:
            for i in range(len(dp) - 1):
                dp.append(dp.pop(1) - dp[0])
            dp.pop(0)

            for item in dp:
                if lower <= item <= upper:
                    num += 1

        return num

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        

if __name__ == '__main__':

    arr1 = [-2, 5, -1]
    arr2 = [0, 0]
    arr3 = [2147483647, -2147483648, -1, 0]
    arr4 = [-2, 5, -1, 0]

    sln = Solution()
    # res = sln.countRangeSum(arr1, -2, 2)
    # res = sln.countRangeSum(arr2, 0, 0)
    res = sln.countRangeSum(arr3, -1, 0)

    print(res)
