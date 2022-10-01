class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l= 0
        hi = len(arr)-1 
        while(l<hi):
            mid = (l+hi)//2
            if arr[mid]  < arr[mid+1]:
                l = mid +1
            else:
                hi = mid
        return l