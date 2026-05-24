class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        map={}
        for i in nums:
            if i in map.keys():
                map[i]+=1
            else:
                map[i]=1
        for i in map.values():
            if i>1:
                return True
        return False