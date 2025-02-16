from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        res = []

        i, j = 0, len(nums) -1

        while i < j:
            
            val = int(str(nums[i]) + str(nums[j]))
            res.append(val)

            i+=1
            j-=1

        if i == j:
            res.append(nums[i])
           
        return sum(res)
    
if __name__ == '__main__':

    """ Example 1: """
    nums = [5,14,13,8,12]
    print(Solution().findTheArrayConcVal(nums))