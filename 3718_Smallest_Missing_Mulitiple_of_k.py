class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while True:
            if i%k==0:
                if i not in nums:
                    return i
                    break

            i+=1



