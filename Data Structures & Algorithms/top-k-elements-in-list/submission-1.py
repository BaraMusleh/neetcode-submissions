import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums: 
            count[num] += 1

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k :
                heapq.heappop(heap)

        out = []
        for pair in heap: 
            out.append(pair[1])

        
        return out 