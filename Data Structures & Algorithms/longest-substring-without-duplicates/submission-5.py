class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        res = 0

        for right, c in enumerate(s):
            if c in last_seen:
                left = max(left, last_seen[c]+1)
            last_seen[c] = right
            res = max(res, right - left + 1)
        return res
            