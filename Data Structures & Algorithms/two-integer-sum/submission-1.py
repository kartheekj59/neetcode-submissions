from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = defaultdict(list)

        for i,v in enumerate(nums):
            indexs[v].append(i)
        for num in nums:
            complement = target-num
            if complement in indexs:
                if complement == num:
                    if len(indexs[complement]) >= 2:
                        return indexs[num][:2]
                else:
                    return [indexs[num][0],indexs[complement][0]]
        return []
                
        

        

        