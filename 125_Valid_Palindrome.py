class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalnum():
                res+=i.lower()
        r=res[::-1]
        return res==r


