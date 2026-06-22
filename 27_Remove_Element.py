class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=[]
        for i in nums:
            if i!=val:
                k.append(i)
        for i in range(len(k)):
            nums[i]=k[i]
        return len(k)

