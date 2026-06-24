class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n=nums1[:m]
        n.extend(nums2)
        n.sort()
        nums1[:]=n