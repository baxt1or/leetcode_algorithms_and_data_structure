from typing import List

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
       """  
       To achive the desired output nums1 and nums2 gets sorted in acsending and descending respectively
       
       returns: dot product of two vectors or arrays
       """
       nums1 = sorted(nums1)
       nums2 = sorted(nums2, reverse=True)

       return sum([x *y for x, y in zip(nums1, nums2)])


""" Example Use  """
nums1 = [5,3,4,2]
nums2 = [4,2,2,5]
Solution().minProductSum(nums1, nums2)