class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_set = set(nums)
        # if len(nums)==len(nums_set):
        #     return False
        # else:
        #     return True
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False          