from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right :
            area = min(height[left], height[right]) * (right - left)
            if area > maxarea :
                maxarea = area

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea


if __name__ == '__main__':
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    sln = Solution()
    res = sln.maxArea(arr)
    print(res)
