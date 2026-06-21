
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        f={}

        for i in t:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for i in s:
            f[i]-=1
        for i in f:
            if f[i]==1:
                return i        