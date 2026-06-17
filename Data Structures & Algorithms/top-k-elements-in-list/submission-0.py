class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        for num in nums:
            if num in mapper:
                mapper[num]+=1
            
            else:
                mapper[num]=1

        sorted_mpr = sorted(mapper.items(), key = lambda x: x[1], reverse = True)

        return [item[0] for item in sorted_mpr[:k]]
