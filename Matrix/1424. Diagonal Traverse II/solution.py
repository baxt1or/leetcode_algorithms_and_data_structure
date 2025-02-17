from typing import List, defaultdict 

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        res = defaultdict(list)

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                res[r+c].append(nums[r][c])
        
        res = dict(sorted(res.items(), key=lambda item:item[0]))

        ans = []

        for row in res.values():
            row.reverse()
            ans.extend(row)
        
        return ans


if __name__ == '__main__':

    """ Example 1: """
    nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    print(Solution().findDiagonalOrder(nums=nums))