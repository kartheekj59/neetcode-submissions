class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)<1:
            return None
        
        ans = [ -1 for i in range(2*len(nums))]
        i = 0; j = len(nums)
        while i < len(nums):
            ans[i] = nums[i]
            ans[j] = nums[i]
            i+=1
            j+=1
        return ans
        