from typing import List
import time

class Solution:
    def findMedianSortedArrays(self, nums1 : List[int], nums2 : List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        len_sum = len_nums1 + len_nums2

        # 如果是奇数，返回中间那个数，如果是偶数，返回中间两个数的均值
        if len_sum % 2 != 0:
            return self.find_kth(nums1, 0, nums2, 0, len_sum // 2 + 1)
        elif len_sum % 2 == 0:
            return ( self.find_kth(nums1, 0, nums2, 0, len_sum // 2) +
                     self.find_kth(nums1, 0, nums2, 0, len_sum // 2 + 1) ) / 2

    # 查找两个数组中第k个数
    def find_kth(self, nums1: List[int], nums1_start:int, nums2:List[int], nums2_start:int, k:int) -> float:
        if nums1_start >= len(nums1):
            return nums2[nums2_start + k - 1]
        if nums2_start >= len(nums2):
            return nums1[nums1_start + k - 1]
        if k == 1:
            return min(nums1[nums1_start], nums2[nums2_start])

        nums1_mid = -1
        nums2_mid = -1
        if nums1_start + k // 2 - 1 < len(nums1):
            nums1_mid = nums1[nums1_start + k // 2 - 1]
        if nums2_start + k // 2 - 1 < len(nums2):
            nums2_mid = nums2[nums2_start + k // 2 - 1]

        if nums1_mid < nums2_mid:
            return self.find_kth(nums1, nums1_start + k // 2, nums2, nums2_start, k - k // 2)
        else:
            return self.find_kth(nums1, nums1_start, nums2, nums2_start + k // 2, k - k // 2)


if __name__ == '__main__':
    start =  time.time()

    sln = Solution()

    num1 = [5, 6]
    num2 = [2, 4]

    pos = sln.findMedianSortedArrays(num1, num2)
    print(pos)

    end = time.time()
    print(str(end - start) + 's')
