class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        for i in range(len(nums)):
            if (target-nums[i]) in map.keys():
                return([map[target-nums[i]],i])
            else:
                map[nums[i]]= i
        
