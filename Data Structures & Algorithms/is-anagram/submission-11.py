class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        map_1={}
        for i in s:
            if i in map.keys():
                map[i]+=1
            else:
                map[i]=1
        for j in t:
            if j in map_1.keys():
                map_1[j]+=1
            else:
                map_1[j]=1
        return map == map_1
            
