class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1= []
        l2= []
        for i in range(0,len(s)):
            if s[i].isalnum():
                l1.append(s[i].lower())
        for j in range(len(s)-1,-1,-1):
            if s[j].isalnum():
                l2.append(s[j].lower())
        return l1 == l2