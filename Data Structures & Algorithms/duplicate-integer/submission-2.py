from collections import namedtuple, deque, defaultdict, Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)

        for num in nums: 
            seen[num] += 1

        for value in seen.values() :
            if value != 1:
                return True

        return False