from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        goal = defaultdict(int)
        left = 0

        for char in s1:
            goal[char] += 1
        
        for right in range(len(s2)):
            count[s2[right]] += 1
            
            if right < len(s1) - 1:
                continue

            left = right - len(s1) + 1

            if count == goal:
                return True

            count[s2[left]] -= 1
            if count[s2[left]] == 0:
                del count[s2[left]]

        return False
            
        

        