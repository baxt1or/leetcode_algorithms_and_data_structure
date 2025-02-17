from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def quad(n, a, b, c):
            return a*(n**2)+b*n+c 
        
        def selectionSort(nums):

            for i in range(len(nums)):
                min_index = i 
                for j in range(i+1, len(nums)):
                    if nums[j] < nums[min_index]:
                        min_index = j 
                nums[i], nums[min_index] = nums[min_index], nums[i]
        
        result = [quad(x,a,b,c) for x in nums]

        selectionSort(result)

        return result
    
if __name__ == '__main__':

    """ Example 1: """
    nums = [-4,-2,2,4]
    a = -1
    b = 3
    c = 5
    print(Solution().sortTransformedArray(nums,a,b,c))