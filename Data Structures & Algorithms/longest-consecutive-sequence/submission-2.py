class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a few checks before continuing
        if not nums:
            return 0
        len_nums = len(nums)
        if len_nums == 1:
            return 1
        nums.sort()
        i = 1
        longest = 1
        # find longest in one pass
        for k in range(0, len_nums - 1):
            kth = nums[k]
            lth = nums[k+1]
            diff = lth - kth
            if diff == 1:
                i += 1
            elif diff == 0:
                continue
            else:
                i = 1
            if i > longest:
                longest = i
            
        return longest