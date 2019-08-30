
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m=len(nums1)
        n=len(nums2)
        sum=0
        if (m+n)%2==0:
            mid1=(m+n)/2
        else:
            mid1=(m+n+1)/2
        i=0
        j=0
        k=1
        while k<m+n+1:
            if k<mid1:
                if i<m and j<n:
                    if nums1[i]<nums2[j]:
                        i=i+1
                    else:
                        j=j+1
                elif not i<m:
                    j=j+1
                elif not j<n:
                    i=i+1
                k=k+1
            elif k==mid1:
                if i<m and j<n:
                    if nums1[i]<nums2[j]:
                        sum = sum + nums1[i]
                        i=i+1
                    else:
                        sum = sum + nums2[j]
                        j=j+1
                elif not i<m:
                    sum = sum + nums2[j]
                    j=j+1
                elif not j<n:
                    sum = sum + nums1[i]
                    i=i+1
                if (m+n)%2==0:
                    if i < m and j < n:
                        if nums1[i] < nums2[j]:
                            sum = sum + nums1[i]
                            i = i + 1
                        else:
                            sum = sum + nums2[j]
                            j = j + 1
                    elif not i < m:
                        sum = sum + nums2[j]
                        j = j + 1
                    elif not j < n:
                        sum = sum + nums1[i]
                        i = i + 1
                    return sum/2
                else:
                    return sum

import time
start=time.clock()
s=Solution()
nums1 = [1,2,4]
nums2 = [3,5]
result=s.findMedianSortedArrays(nums1,nums2)
print(result)
print("time",(time.clock()-start)*1000)


