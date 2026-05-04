class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       temp = {}
       for i in range(0,len(nums)):
        if (target - nums[i]) in temp.keys():
                return [temp[target-nums[i]],i]
        elif nums[i] not in temp.keys():
            temp[nums[i]] = i
        

            
        
        