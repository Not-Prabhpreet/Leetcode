class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map= {}
        arr_values= []
        for i in range(len(nums)):
            if nums[i] in hash_map.keys():
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]] = 1
        tup = hash_map.items()
        tup = list(tup)
        tup = sorted(tup, key = lambda x:x[1])
        for i in tup:
            arr_values.append(i[0])
        return arr_values[len(arr_values)-k : len(arr_values)]

        