class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        arr=[]
        for i in nums:
            if arr.count(i)<k:
                arr.append(i)
        
        return arr