from typing import List

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
     
        ans = self.flatten(mat)

        count = {}

        for n in ans:
            count[n] = count.get(n, 0)+1
        
        result = [key for key, val in count.items() if val == len(mat)]

        return min(result) if result else -1
    
    def flatten(self, mat):
        res = []

        for row in mat:
            if isinstance(row, list):
                res.extend(self.flatten(row))
            else:
                res.append(row)
        return res

if __name__ == "__main__":
   
    sol = Solution()

    """ Example 1: """
    mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
    print(sol.smallestCommonElement(mat))

    """ Example 2: """
    mat = [[1,2,3],[2,3,4],[2,3,5]]
    print(sol.smallestCommonElement(mat))
