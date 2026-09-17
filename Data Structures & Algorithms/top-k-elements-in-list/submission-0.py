from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        ans = []
        for key,v in freq.items():
            ans.append((-v,key))
        heapq.heapify(ans)

        res = []

        while k!=0:
            t = heapq.heappop(ans)
            res.append(t[1])
            k-=1
        return res



        