from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        som = 0
        nums = []
        nums2 = []

        for i in range(len(mat)):
            nums.append(mat[i][i])
            nums2.append(mat[i][len(mat)-1-i])
        
        mid = len(nums)//2

        if len(mat) % 2 == 0:
            som = sum(nums) + sum(nums2)
        
        elif nums[mid] == nums2[mid]:
            nums2.remove(nums2[mid])
            
            som = sum(nums+nums2)

        return som


if __name__ == "__main__":

    """ Example 1: """
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().diagonalSum(mat=mat))


    """ Example 2: """
    mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    print(Solution().diagonalSum(mat=mat))


    """ Example 3: """
    mat = [[4,6,7],[2,9,4],[5,5,5]]
    print(Solution().diagonalSum(mat=mat))