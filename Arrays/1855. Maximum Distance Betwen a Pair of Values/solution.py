from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        max_distance = 0
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):

          if nums1[i] <= nums2[j] and j < len(nums2):
            max_distance = max(max_distance, j-i)
            j+=1
          else:
            i+=1
        return max_distance

if __name__ == '__main__':
   
   """ Example 1: """
   nums1 = [55,30,5,4,2]
   nums2 = [100,20,10,10,5]
   print(Solution().maxDistance(nums1, nums2))