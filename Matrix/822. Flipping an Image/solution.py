from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in image:
          row.reverse()
        
        
        for row in image:
          for i in range(len(row)):
            if row[i] == 0:
              row[i] = 1
            else:
              row[i] = 0
        
        return image


if __name__ == '__main__':
   
   """ Example 1: """
   image = [[1,1,0],[1,0,1],[0,0,0]]
   print(Solution().flipAndInvertImage(image=image))


   """ Example 2: """
   image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
   print(Solution().flipAndInvertImage(image=image))