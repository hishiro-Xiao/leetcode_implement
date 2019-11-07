from typing import List


class Solution:
    def commonPrefix(self, str1: str, str2: str) -> str:
        min_size = min(len(str1), len(str2))
        common_prefix = 0
        for i in range(min_size):
            if str1[i] == str2[i]:
                common_prefix += 1
            else:
                break
        return str1[0: common_prefix]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        longest_common_prefix = self.commonPrefix(strs[0], strs[1])

        for i in range(2, len(strs)):
            if len(longest_common_prefix) == 0:
                return ''
            minlen = min(len(longest_common_prefix), len(strs[i]))
            common = 0
            for index in range(minlen):
                if strs[i][index] == longest_common_prefix[index]:
                    common += 1
            longest_common_prefix = strs[i][0: common]

        return longest_common_prefix

if __name__ == '__main__':

    arr = ['flower', 'flow', 'flag']
    arr2 = ['dog', 'cat', 'frog']

    sln = Solution()
    res = sln.longestCommonPrefix(arr2)

    # res1 = sln.commonPrefix('flower', 'dog')
    print(res)
