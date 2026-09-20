class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            needed = current_sum % k

            if needed in remainders and i - remainders[needed] >= 2:
                return True

            if needed not in remainders:
                remainders[needed] = i

        return False