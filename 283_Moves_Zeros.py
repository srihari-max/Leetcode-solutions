class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[]
        res=[]
        for i in nums:
            if i==0:
                arr.append(i)
            else:
                res.append(i)
        res.extend(arr)
        nums[:]=res
