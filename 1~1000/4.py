class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        length = len(arr)
        return (arr[length//2-1] + arr[length//2]) / 2 if length % 2 == 0 else arr[length//2]
