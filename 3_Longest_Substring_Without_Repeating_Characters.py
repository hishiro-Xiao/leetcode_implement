
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        hashmap = set()
        max_of_substring = 0

        for i in range(len(s)):
            while s[i] in hashmap:
                hashmap.remove(s[start])
                start += 1
            hashmap.add(s[i])
            max_of_substring = max(max_of_substring, len(hashmap))

        return max_of_substring

if __name__ == '__main__':
    sln = Solution()

    s = (
        'abcabcbb',
        'pwwkew',
        'bbbbbb',
        'aab',
        'dvdf'
    )

    for i in range(len(s)):
        maxLength_substring = sln.lengthOfLongestSubstring(s[i])
        print(s[i] + ' : ', end='')
        print(maxLength_substring)
