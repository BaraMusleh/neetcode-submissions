class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])

        suffix = [1]
        for i in range (len(nums) - 2, -1, -1):
            suffix.append(suffix[-1] * nums[i+1])
        suffix.reverse()

        out = []
        for i in range(len(nums)):
            out.append(prefix[i] * suffix[i])

        return out