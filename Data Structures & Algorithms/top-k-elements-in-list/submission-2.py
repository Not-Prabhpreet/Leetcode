class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for element in nums:
            if element in map:
                map[element]+=1
            else:
                map[element]=1 
        temp = [[] for i in range(0,len(nums)+1)]
        for i in map.keys():
            temp[map[i]].append(i)
        ans = []
        for arr in range(len(temp)-1, 0, -1):
            for j in temp[arr]:
                ans.append(j)
                if len(ans) == k:
                    return ans
        
        
