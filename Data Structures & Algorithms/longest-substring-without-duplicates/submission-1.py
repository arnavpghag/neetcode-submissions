class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        not_duplicate = set()

        for right in range(len(s)):

            while s[right] in not_duplicate:
                not_duplicate.remove(s[left])
                left += 1

            not_duplicate.add(s[right])

            longest = max(longest, right - left + 1)

        return longest