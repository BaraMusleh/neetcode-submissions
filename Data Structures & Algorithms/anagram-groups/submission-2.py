from collections import namedtuple, deque, defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counter = defaultdict(list)
        out = set()
        for word in strs : 
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord('a')] += 1
            
            counter[tuple(arr)].append(word)

        return list(counter.values())
            
        