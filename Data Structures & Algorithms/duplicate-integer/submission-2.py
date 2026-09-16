class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        membership = set()
        for i in nums:
            if i in membership:
                return True
            else:
                membership.add(i)
        return False

        