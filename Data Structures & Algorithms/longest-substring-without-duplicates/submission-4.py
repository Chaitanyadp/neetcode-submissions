class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in last_seen:
                last_seen.remove(s[l])
                l += 1
            last_seen.add(s[r])
            res = max(res, r - l + 1)
        return res
