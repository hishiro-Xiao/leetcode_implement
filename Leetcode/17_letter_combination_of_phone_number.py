from typing import List
import itertools

class Solution:

    # 我的解法
    # # 传入一个1到9的数字，按照其在9键键盘上的位置，返回能打出的字母数组
    # def getNumber(self, digit: str):
    #     backup = '####abc#def#ghi#jkl#mno#pqrstuv#wxyz'
    #     str_number = int(digit) - 1
    #     random_number = str_number * 4
    #     if str_number != 6 and str_number != 8:
    #         sublen = 3
    #     else:
    #         sublen = 4
    #
    #     return backup[random_number: random_number+sublen]
    #
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if len(digits) == 0:
    #         return []
    #     if len(digits) == 1:
    #         result = []
    #         numbers = self.getNumber(digits)
    #         for i in numbers:
    #             result.append(i)
    #         return result
    #
    #     result = []
    #     for x in itertools.product(self.getNumber(digits[0]), self.getNumber(digits[1])):
    #         tmp = ''.join(x)
    #         result.append(tmp)
    #
    #     pos = 0
    #     while pos < len(digits) - 2:
    #         new_res = []
    #         for x in itertools.product(result, self.getNumber(digits[2 + pos])):
    #             tmp = ''.join(x)
    #             new_res.append(tmp)
    #         result = new_res
    #         pos += 1
    #
    #     return result

    # 回溯法
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def backtrack(self, result: List[str], combination: str, remain_digits: str):
        if remain_digits == '':
            return result.append(combination)
        else:
            for digit_number in self.phone[remain_digits[0]]:
                self.backtrack(result, combination + digit_number, remain_digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) <= 0:
            return []

        self.backtrack(result, '', digits)
        return result


if __name__ == '__main__':
    number = "2"

    sln = Solution()
    res = sln.letterCombinations(number)
    # res1 = sln.getNumber(number)
    print(res)
    # print(len(res))
