from collections import namedtuple, deque, defaultdict, Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        counter = defaultdict(int)

        for char in s:
            counter[char] += 1

        for char in t: 
            counter[char] -= 1

        for value in counter.values():
            if value != 0:
                return False
        
        return True


        