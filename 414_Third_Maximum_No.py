class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l=set(nums)
        s=list(l)
        s.sort(reverse=True)
        if len(s)>=3:
            return s[2]
        return s[0]
