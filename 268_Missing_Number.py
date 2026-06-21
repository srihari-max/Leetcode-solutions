class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=[]
        for i in range(len(nums)+1):
            n.append(i)
        
        for i in n:
            if i not in nums:
                return i
                break