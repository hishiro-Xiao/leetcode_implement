from typing import List
import itertools

class Solution:
    # 检查表达式的括号是否合法
    def isLeagl(self, expression: str):
        exp = [i for i in expression]
        stack = []
        for para in exp:
            if para == '(':
                stack.append('(')
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True

    # # 我的解法: 回溯法
    #     # def generateParenthesis(self, n: int) -> List[str]:
    #     #     if n <= 0:
    #     #         return []
    #     #
    #     #     result = []
    #     #
    #     #     def backtrack(expr: str, depth: int):
    #     #         if depth == 0:
    #     #             if self.isLeagl(expr):
    #     #                 result.append(expr)
    #     #             return
    #     #         else:
    #     #             backtrack(expr + '(', depth - 1)
    #     #             backtrack(expr + ')', depth - 1)
    #     #
    #     #     backtrack('(', n * 2 - 1)
    #     #     return result

    # dalao的动态规划解法
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = [[''], ['()']]

        for index in range(2, n+1):
            tmp_res = []
            for p in range(0, index):
                q = index - p - 1

                left_choice = result[p]
                right_choice = result[q]

                for x in itertools.product(left_choice, right_choice):
                    left_part = '(' + x[0] + ')'
                    right_part = x[1]
                    tmp_res.append(left_part + right_part)

            result.append(tmp_res)

        return result[n]


if __name__ == '__main__':
    string = ''

    sln = Solution()
    res = sln.generateParenthesis(3)
    # res = sln.isLeagl(string)
    print(res)
