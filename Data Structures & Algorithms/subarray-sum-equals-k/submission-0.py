from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = {0:1}
        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            prev_sum = current_sum - k
            count += prefix_sum.get(prev_sum, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count

        