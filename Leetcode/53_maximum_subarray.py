from typing import List


class Solution:
    # 暴力法 时间复杂度O(n^2)
    def maxSubArray_1(self, nums: List[int]) -> int:
        len_nums = len(nums)
        distance = {}

        for i in range(len_nums):
            for j in range(i, len_nums):
                distance[str(i) + ',' + str(j)] = sum(nums[i:j+1])

        print(distance)
        return max(distance.values())

    # 暴力法2  时间复杂度O(n)
    def maxSubArray_2(self, nums: List[int]) -> int:
        cur_max = nums[0]
        max_sum = cur_max

        for i in range(1, len(nums)):
            if cur_max + nums[i] > nums[i]:
                max_sum = max(cur_max + nums[i], max_sum)
                cur_max = cur_max + nums[i]
            else:
                max_sum = max(max_sum, nums[i])
                cur_max = nums[i]

        return max_sum

    # 分治 时间复杂度O(nlogn)
    def maxSubArray_3(self, nums: List[int]) -> int:
        len_nums = len(nums)

        if len_nums == 1 :
            return nums[0]
        else:
            max_left = self.maxSubArray_3(nums[0: len_nums // 2 - 1])
            max_right = self.maxSubArray_3(nums[len_nums // 2 : len_nums])

        max_l = nums[len_nums // 2 - 1]
        cur = 0
        for i in range(len_nums // 2 - 1, -1, -1):
            cur += nums[i]
            max_l = max(cur, max_l)
        max_r = nums[len_nums // 2]
        cur = 0
        for i in range(len_nums // 2, len_nums):
            cur += nums[i]
            max_r = max(cur, max_r)

        return max(max_left, max_right, max_l + max_r)

if __name__ == '__main__':
    sln = Solution()

    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums2 = [0, -2, 3, 5, -1, 2]
    nums3 = [-9, -2, -3, -5, -3]
    nums4 = [0, 1, 2]

    max = sln.maxSubArray_3(nums1)
    print('Maximum sum : ' + str(max))
