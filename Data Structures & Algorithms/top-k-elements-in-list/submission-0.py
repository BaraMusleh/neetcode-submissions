from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        arr = []
        max = 0
        out = None
        for num in nums: 
            count[num] += 1

        for n in range(k): 
            for key, value in count.items():
                if value > max and key not in arr: 
                    max = value
                    out = key

            max = 0 
            arr.append(out)

        return arr