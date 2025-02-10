from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nums = []

        for row in matrix:
            nums.extend(row)
                

        l, r = 0, len(nums) - 1

        while l <= r:
          mid = (l+r) // 2
          if nums[mid] == target:
            return True
          if nums[mid] < target:
            l = mid + 1
          else:
            r = mid - 1
        return False


if __name__ == "__main__":
   
   """ Example 1: """
   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target = 3
   print(Solution().searchMatrix(matrix=matrix, target=target))

   """ Example 2: """
   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target = 13
   print(Solution().searchMatrix(matrix=matrix, target=target))