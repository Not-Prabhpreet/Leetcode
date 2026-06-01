class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in strs:
            ls = [0] * 26
            for c in i:
                ls[ord(c) - ord('a')] += 1
            if tuple(ls) in map:
                map[tuple(ls)].append(i) 
            else:
                map[tuple(ls)] = [i]    
        
        return list(map.values())