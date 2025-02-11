from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        l, r = 0, len(arr) -1
        ans = -1

        while l <= r:
          mid = (l+r) //2

          if arr[mid] == mid:
            ans = mid
            r = mid -1
          elif arr[mid] < mid:
            l = mid+1
          else:
            r = mid -1
        return ans

if __name__ == "__main__":
    
    """ Example 1: """
    arr = [-10,-5,0,3,7]
    print(Solution().fixedPoint(arr=arr))