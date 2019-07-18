class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        List = sorted(nums1 + nums2)
        x = len(List)
        y = x // 2
        if x % 2 == 0:
            return (List[y - 1] + List[y]) / 2
        else:
            return List[y]
        
