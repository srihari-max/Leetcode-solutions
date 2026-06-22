class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        res=""
        for i in reversed(s):
            res=res+" "+i
        return res.strip()
            
        