class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        this_dict={}
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) not in this_dict.keys():
                this_dict["".join(sorted(strs[i]))] = [strs[i]]
            else:
                this_dict["".join(sorted(strs[i]))].append(strs[i])
        return list(this_dict.values())