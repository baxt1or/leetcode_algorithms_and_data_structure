from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        s = len(nums1) - m

        while s != 0:
            nums1.pop()
            s-=1
        
        nums1.extend(nums2[:n])
        
        for i in range(len(nums1)):
            min_index = i 
            for j in range(i+1, len(nums1)):
                if nums1[j] < nums1[min_index]:
                    min_index = j 
            nums1[i], nums1[min_index] = nums1[min_index], nums1[i]

if __name__ == '__main__':

    """ Example 1: """
    nums1 = [-1,0,0,3,3,3,0,0,0]
    m = 6
    nums2 = [1,2,2]
    n = 3
    Solution().merge(nums1=nums1, m=m,nums2=nums2,n=n)
    print(nums1)