class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        start = []
        length = []
        max = 0
        for num in nums_set:
            c = 1
            if num-1 not in nums_set:
                while num+1 in nums_set:
                    c+=1
                    num = num + 1
                if c>max:
                    max = c
        return max
                