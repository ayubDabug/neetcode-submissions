from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)

        for item in nums:
            if item not in d:
                d[item] = 1
            else:
                return True
        return False