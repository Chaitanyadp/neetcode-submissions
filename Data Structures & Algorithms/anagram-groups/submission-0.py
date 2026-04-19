class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            # in python list cannot be keys(cuz they are mutable), so we have changed to tuple as its immutable
            res[tuple(count)].append(s) 
        return list(res.values())


        # O(m.n) time      

        # If I ask for a key that doesn't exist, 
        # automatically create it and give it a default value of an empty list
        # if append is used then after creation it appends the value

        # another Solution slower Time complexity: O(m.nlogn) Space complexity: O(m.n)
        # res = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))
        #     res[key].append(s)
        # return list(res.values())    