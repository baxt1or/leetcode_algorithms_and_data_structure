from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, row = [], []

        def backtrack():
            if len(row) == n:
                res.append(row.copy())
                return
            
            for x in nums:
                if x not in row:
                    row.append(x)
                    backtrack()
                    row.pop()
        
        backtrack()
        return res 
    

if __name__ == '__main__':
    """ Example 1: """
    nums = [1,2,3]
    print(Solution().permute(nums))