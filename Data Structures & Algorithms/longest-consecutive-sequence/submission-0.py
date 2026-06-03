class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        start = []
        length = []
        for num in nums_set:
            if num-1 not in nums_set:
                start.append(num)
        for num in start:
            c = 1
            while num+1 in nums_set:
                c+=1
                num = num + 1
            length.append(c)
        return max(length)
