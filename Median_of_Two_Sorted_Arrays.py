class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        length=len(num)
        if(length%2==0):
            median=(num[int(length/2)-1]+num[int(length/2)])/2
        else:
            median=num[int((length-1)/2)]
        return(median)
