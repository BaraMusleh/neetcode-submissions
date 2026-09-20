class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        wantedNumber = {}
        out = set()
        for i, num in enumerate(nums): 
            if num in wantedNumber:
                return [wantedNumber[num], i]
                
            wantedNumber[target - num] = i

        return []
            
                


        