from heapq import heappush, heappop
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def check(k,l,odd):
            if odd:
                if l//2==k:
                    return (k,k)
            else:
                if l//2==k:
                    return (k-1,k)
            return None

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
        odd=(n+m)&1==1
        i,j=0,0
        ms=[0]*(n+m)
        k=0
        while i<n or j<m:
            if j==m or i<n and nums1[i]<nums2[j]:
                ms[k]=nums1[i]
                i+=1
            else:
                ms[k]=nums2[j]
                j+=1
            res = check(k,n+m,odd)
            # print(ms)
            if res:
                return (ms[res[0]]+ms[res[1]])/2
            k+=1
