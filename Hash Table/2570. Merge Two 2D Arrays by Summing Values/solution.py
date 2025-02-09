from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
      
      count = {}

      for row in nums1:
        count[row[0]] = row[1]
      
      for row in nums2:
        if row[0] in count.keys():
          count[row[0]] = row[1] + count[row[0]]
        else:
          count[row[0]] = row[1]
      
      return sorted([[key, val] for key, val in count.items()], key=lambda item: item[0])