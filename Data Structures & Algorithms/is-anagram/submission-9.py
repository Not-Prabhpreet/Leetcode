class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        this_dict = {}
        for letter in s:
            if letter in this_dict:
                this_dict[letter]+=1
            else:
                this_dict[letter] = 1
        for letter in t:
            if letter in this_dict.keys():
                this_dict[letter] -=1
            else:
                return False
        for i in this_dict.values():
            if i!=0:
                return False
        
        return True