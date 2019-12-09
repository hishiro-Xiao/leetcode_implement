from typing import List

# 解法1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)
#         j = -1
#         for i in range(length):
#             if target - nums[i] in nums:
#                 if nums.index(target - nums[i]) == i:
#                     continue
#                 else:
#                     j = nums.index(target - nums[i])
#                     break
#
#         if j == -1:
#             return []
#         else:
#             return [i, j]

# 解法2
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)
#         j = -1
#
#         for i in range(1, length):
#             temp = nums[:i]
#             if target - nums[i] in temp:
#                 j = temp.index(target - nums[i])
#                 break
#
#         if j == -1:
#             return []
#         elif j >= 0:
#             return [i, j]

# 解法3 哈希查找
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - nums[i])
            if j is not None and i != j:
                return [i, j]

if __name__ == "__main__":

    sln = Solution()
    res = sln.twoSum([2, 7, 11, 15, 2], 4)

    print(res)
