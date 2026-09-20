class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        best = float('inf')
        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                best = min(best, right - left + 1)
                current_sum -= nums[left]
                left += 1
            
        return best if best != float('inf') else 0
                
            