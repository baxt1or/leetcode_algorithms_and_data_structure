from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_val = -1

        for i in range(len(arr)-1, -1, -1):
          
          max_val = max(max_val, arr[i])
          arr[i] = max_val
        
        arr.append(-1)
        return arr[1:]

if __name__ == '__main__':
   
   """ Example 1: """
   arr = [17,18,5,4,6,1]
   print(Solution().replaceElements(arr))

   """ Example 2: """
   arr = [400]
   print(Solution().replaceElements(arr))