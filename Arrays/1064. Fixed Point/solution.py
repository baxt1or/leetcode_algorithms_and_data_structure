from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        for i in range(len(arr)):
            if arr[i] == i:
                return i
        return -1

if __name__ == "__main__":
    
    """ Example 1: """
    arr = [-10,-5,0,3,7]
    print(Solution().fixedPoint(arr=arr))