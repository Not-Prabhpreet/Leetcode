class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = []
        p1= 1
        for i in range(1,len(nums)):
            p1*= nums[i-1]
            left_array.append(p1)
        left_array.insert(0,1)

        right_array = []
        p2 = 1
        for j in range(len(nums)-2,-1,-1):
            p2*=nums[j+1]
            right_array.insert(0,p2)
        right_array.append(1)
        ans = []
        for p in range(0,len(left_array)):
            ans.append(right_array[p] * left_array[p])
        return ans