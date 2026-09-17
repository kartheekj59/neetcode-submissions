class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        should_not_be_val = 0
        should_be_val = len(nums)-1

        while should_not_be_val <= should_be_val:
            if nums[should_not_be_val] == val and nums[should_be_val]!= val:
                nums[should_not_be_val] = nums[should_be_val]
                nums[should_be_val] = val
                should_be_val-=1
                should_not_be_val+=1
            elif nums[should_not_be_val] != val:
                should_not_be_val+=1
            elif nums[should_be_val] == val:
                should_be_val-=1
        return should_not_be_val

        

        