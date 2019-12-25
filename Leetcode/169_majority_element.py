from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sta = {}
        for num in nums:
            if not sta.__contains__(num):
                sta[num] = 1
            else:
                sta[num] += 1
        
        return max(sta.keys(), key=sta.get)

    def majorityElement2(self, nums: List[int]) -> int:
        sta = {}
        max_num = 1
        max_obj = nums[0]

        for num in nums:
            if num not in sta.keys():
                sta[num] = 1
            else:
                sta[num] += 1
                if sta[num] > max_num:
                    max_num = sta[num]
                    max_obj = num
                if max_num > len(nums) // 2:
                    return max_obj
        
        return max_obj

    # 官方解法1：哈希表，时间复杂度O(n)，空间复杂度O(n)
    def majorityElement3(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # 官方解法1：Boyer-Moore 投票算法，时间复杂度O(n)，空间复杂度O(1)   卧槽
    def majorityElement4(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            else:
                if num != candidate:
                    count -= 1
                else:
                    count += 1

        return candidate

if __name__ == '__main__':
    
    arr1 = [3,2,3]
    arr2 = [2,2,1,1,1,2,2]
    arr3 = [6,6,6,7,7]
    arr4 = [1]

    sln = Solution()
    res = sln.majorityElement4(arr3)
    print(res)
