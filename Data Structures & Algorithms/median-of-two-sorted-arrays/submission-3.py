from heapq import heappush, heappop
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        if n==0:
            if m&1:
                return nums2[m//2]
            else:
                return (nums2[m//2]+nums2[m//2-1])/2
        elif m==0:
            if n&1:
                return nums1[n//2]
            else:
                return (nums1[n//2]+nums1[n//2-1])/2
        minhlen=(n+m)//2+1
        maxhlen=(n+m)//2+1
        minh,maxh=[],[]
        for i in nums1:
            heappush(minh,-i)
            heappush(maxh,i)
        for i in nums2:
            heappush(minh,-i)
            heappush(maxh,i)
        while len(minh)>minhlen:
            heappop(minh)
        while len(maxh)>maxhlen:
            heappop(maxh)
        # print(minh,maxh,minhlen,maxhlen)
        return (heappop(maxh)-heappop(minh))/2